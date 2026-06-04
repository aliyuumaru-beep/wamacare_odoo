from odoo import models, fields, api


class WamaCase(models.Model):
    """BEN-008: Case Management — one case per beneficiary concern."""
    _name = 'wamacare.case'
    _description = 'WamaCare Beneficiary Case'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_opened desc'
    _rec_name = 'name'

    name = fields.Char(
        string='Case Reference',
        readonly=True,
        default='New',
        copy=False,
    )
    beneficiary_id = fields.Many2one(
        'res.partner',
        string='Beneficiary',
        required=True,
        domain=[('category_id.name', 'ilike', 'Beneficiary')],
        tracking=True,
    )
    case_type = fields.Selection([
        ('safeguarding',  'Safeguarding'),
        ('health',        'Health & Wellbeing'),
        ('legal',         'Legal Support'),
        ('economic',      'Economic Empowerment'),
        ('gbv',           'Gender-Based Violence'),
        ('other',         'Other'),
    ], string='Case Type', required=True, default='safeguarding', tracking=True)

    severity = fields.Selection([
        ('low',      'Low'),
        ('medium',   'Medium'),
        ('high',     'High'),
        ('critical', 'Critical — Immediate Action Required'),
    ], string='Severity', required=True, default='medium', tracking=True)

    state = fields.Selection([
        ('open',       'Open'),
        ('in_progress','In Progress'),
        ('escalated',  'Escalated'),
        ('referred',   'Referred'),
        ('closed',     'Closed'),
    ], string='Status', default='open', tracking=True, group_expand='_expand_states')

    description = fields.Text(
        string='Case Description',
        help='Describe the concern or need. Keep factual and objective.',
    )
    date_opened = fields.Datetime(
        string='Opened',
        default=fields.Datetime.now,
        readonly=True,
    )
    date_closed = fields.Datetime(
        string='Closed On',
        readonly=True,
    )
    assigned_to = fields.Many2one(
        'hr.employee',
        string='Assigned To',
        tracking=True,
    )
    programme_id = fields.Many2one(
        'project.project',
        string='Related Programme',
    )

    # ── BEN-009: Case Notes ───────────────────────────────────
    note_ids = fields.One2many(
        'wamacare.case.note',
        'case_id',
        string='Case Notes',
    )
    note_count = fields.Integer(compute='_compute_note_count', string='Notes')

    # ── SAFE-007: Evidence ────────────────────────────────────
    evidence_description = fields.Text(
        string='Evidence Description',
        help='Describe any evidence collected (documents, photos, witness statements).',
    )

    # ── SAFE-008: Referral ────────────────────────────────────
    referral_agency = fields.Char(
        string='Referred To',
        help='Name of external agency, hospital, police, NGO, etc.',
        tracking=True,
    )
    referral_date = fields.Date(string='Referral Date', tracking=True)
    referral_notes = fields.Text(string='Referral Notes')
    referral_outcome = fields.Text(
        string='Referral Outcome',
        help='What happened after the referral?',
    )

    @api.depends('note_ids')
    def _compute_note_count(self):
        for rec in self:
            rec.note_count = len(rec.note_ids)

    def _expand_states(self, states, domain, order):
        return ['open', 'in_progress', 'escalated', 'referred', 'closed']

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('wamacare.case') or 'New'
        return super().create(vals_list)

    # ── SAFE-006: Escalation ──────────────────────────────────
    def action_escalate(self):
        """Escalate case to Safeguarding Lead and record escalation note."""
        self.ensure_one()
        lead = self.env['hr.employee'].search(
            [('job_id.name', 'ilike', 'Safeguarding')], limit=1
        )
        self.write({'state': 'escalated', 'assigned_to': lead.id if lead else self.assigned_to.id})
        self.env['wamacare.case.note'].create({
            'case_id':   self.id,
            'note_type': 'escalation',
            'note':      f'Case escalated to {lead.name if lead else "Safeguarding Lead"}.',
        })
        if lead and lead.user_id:
            self.message_notify(
                partner_ids=[lead.user_id.partner_id.id],
                subject=f'CASE ESCALATED — {self.name} / {self.beneficiary_id.name}',
                body=(
                    f'Case <b>{self.name}</b> for beneficiary '
                    f'<b>{self.beneficiary_id.name}</b> has been escalated to you.<br/>'
                    f'Severity: <b>{dict(self._fields["severity"].selection).get(self.severity)}</b><br/>'
                    f'Please review and take action immediately.'
                ),
            )
        return True

    def action_refer(self):
        self.write({'state': 'referred'})
        self.env['wamacare.case.note'].create({
            'case_id':   self.id,
            'note_type': 'referral',
            'note':      f'Case referred to: {self.referral_agency or "external agency"} on {self.referral_date}.',
        })

    def action_close(self):
        self.write({'state': 'closed', 'date_closed': fields.Datetime.now()})
        self.env['wamacare.case.note'].create({
            'case_id':   self.id,
            'note_type': 'closure',
            'note':      'Case closed.',
        })

    def action_reopen(self):
        self.write({'state': 'open', 'date_closed': False})

    def action_add_note(self):
        """Open a dialog to add a case note with evidence file upload."""
        self.ensure_one()
        return {
            'type':      'ir.actions.act_window',
            'name':      'Add Note / Upload Evidence',
            'res_model': 'wamacare.case.note',
            'view_mode': 'form',
            'view_id':   self.env.ref('wamacare_safeguarding.view_wamacare_case_note_form').id,
            'target':    'new',
            'context':   {
                'default_case_id':   self.id,
                'default_note_type': 'evidence',
            },
        }


class WamaCaseNote(models.Model):
    """BEN-009: Timestamped case notes."""
    _name = 'wamacare.case.note'
    _description = 'WamaCare Case Note'
    _order = 'date desc'

    case_id = fields.Many2one(
        'wamacare.case',
        string='Case',
        required=True,
        ondelete='cascade',
    )
    note_type = fields.Selection([
        ('update',     'Progress Update'),
        ('escalation', 'Escalation'),
        ('referral',   'Referral'),
        ('evidence',   'Evidence'),
        ('closure',    'Closure'),
        ('other',      'Other'),
    ], string='Note Type', default='update', required=True)
    note = fields.Text(string='Note', required=True)
    date = fields.Datetime(
        string='Date & Time',
        default=fields.Datetime.now,
        readonly=True,
    )
    author_id = fields.Many2one(
        'res.users',
        string='Recorded By',
        default=lambda self: self.env.uid,
        readonly=True,
    )
    attachment_ids = fields.Many2many(
        'ir.attachment',
        string='Evidence Attachments',
        help='Attach supporting documents, photos, or reports (SAFE-007)',
    )
