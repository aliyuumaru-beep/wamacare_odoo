from odoo import models, fields, api
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # ── BEN-007: Consent Tracking ─────────────────────────────
    x_consent_given = fields.Boolean(
        string='Consent Given',
        default=False,
        help='Has this beneficiary given informed consent for data collection and processing?',
        tracking=True,
    )
    x_consent_date = fields.Date(
        string='Consent Date',
        help='Date consent was obtained',
        tracking=True,
    )
    x_consent_method = fields.Selection([
        ('verbal',   'Verbal (witnessed)'),
        ('written',  'Written signature'),
        ('guardian', 'Guardian consent (minor)'),
    ], string='Consent Method', tracking=True)
    x_consent_notes = fields.Text(
        string='Consent Notes',
        help='Additional notes about the consent obtained',
    )

    # ── SAFE-005: Safeguarding Alert Flag ─────────────────────
    x_safeguarding_flag = fields.Boolean(
        string='Safeguarding Concern',
        default=False,
        help='Flag this record for safeguarding review. Triggers notification to Safeguarding Lead.',
        tracking=True,
    )
    x_safeguarding_flag_date = fields.Datetime(
        string='Flag Raised On',
        readonly=True,
    )
    x_safeguarding_flag_raised_by = fields.Many2one(
        'res.users',
        string='Flag Raised By',
        readonly=True,
    )
    x_safeguarding_flag_reason = fields.Text(
        string='Concern Description',
        help='Describe the safeguarding concern. This is confidential.',
    )
    x_safeguarding_status = fields.Selection([
        ('open',     'Open — Pending Review'),
        ('reviewed', 'Reviewed — Action Taken'),
        ('cleared',  'Cleared — No Action Required'),
        ('referred', 'Referred to External Agency'),
    ], string='Safeguarding Status', default='open', tracking=True)

    # ── Case relationship ─────────────────────────────────────
    x_case_ids = fields.One2many(
        'wamacare.case',
        'beneficiary_id',
        string='Case Records',
    )
    x_case_count = fields.Integer(
        string='Cases',
        compute='_compute_case_count',
    )

    @api.depends('x_case_ids')
    def _compute_case_count(self):
        for rec in self:
            rec.x_case_count = len(rec.x_case_ids)

    # ── SAFE-005: Auto-stamp when flag is raised ──────────────
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('x_safeguarding_flag'):
                vals['x_safeguarding_flag_date'] = fields.Datetime.now()
                vals['x_safeguarding_flag_raised_by'] = self.env.uid
        return super().create(vals_list)

    def write(self, vals):
        # Stamp date and user when flag is first raised
        if vals.get('x_safeguarding_flag') and not self.x_safeguarding_flag:
            vals['x_safeguarding_flag_date'] = fields.Datetime.now()
            vals['x_safeguarding_flag_raised_by'] = self.env.uid
            # Auto-create a case for flagged beneficiaries
            self._create_safeguarding_case(vals.get('x_safeguarding_flag_reason', ''))
        # Clear stamp if flag is removed
        if 'x_safeguarding_flag' in vals and not vals['x_safeguarding_flag']:
            vals['x_safeguarding_flag_date'] = False
            vals['x_safeguarding_flag_raised_by'] = False
        return super().write(vals)

    def action_view_cases(self):
        self.ensure_one()
        return {
            'type':      'ir.actions.act_window',
            'name':      f'Cases — {self.name}',
            'res_model': 'wamacare.case',
            'view_mode': 'list,kanban,form',
            'domain':    [('beneficiary_id', '=', self.id)],
            'context':   {'default_beneficiary_id': self.id},
        }

    def _create_safeguarding_case(self, reason):
        """SAFE-006: Auto-create a case and notify Safeguarding Lead when flag is raised."""
        for partner in self:
            # Find the Safeguarding Lead employee
            lead = self.env['hr.employee'].search(
                [('job_id.name', 'ilike', 'Safeguarding')], limit=1
            )
            case = self.env['wamacare.case'].create({
                'beneficiary_id': partner.id,
                'case_type':      'safeguarding',
                'severity':       'high',
                'state':          'open',
                'description':    reason or 'Safeguarding concern flagged — details pending.',
                'assigned_to':    lead.id if lead else False,
            })
            # Post chatter message on the partner record
            partner.message_post(
                body=(
                    f'<b>⚠ Safeguarding concern raised</b><br/>'
                    f'Case <b>{case.name}</b> has been opened automatically.<br/>'
                    f'Assigned to: {lead.name if lead else "Safeguarding Lead (unassigned)"}.<br/>'
                    f'Reason: {reason or "Not specified."}'
                ),
                message_type='comment',
                subtype_xmlid='mail.mt_note',
            )
            # Notify the Safeguarding Lead user if they have a linked user
            if lead and lead.user_id:
                case.message_notify(
                    partner_ids=[lead.user_id.partner_id.id],
                    subject=f'SAFEGUARDING CONCERN — {partner.name}',
                    body=(
                        f'A safeguarding concern has been flagged for beneficiary '
                        f'<b>{partner.name}</b>.<br/>'
                        f'Please review Case <b>{case.name}</b> immediately.<br/>'
                        f'Reason: {reason or "Not specified."}'
                    ),
                )
