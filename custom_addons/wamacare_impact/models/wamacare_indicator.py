from odoo import models, fields, api


class WamaCareIndicator(models.Model):
    """ME-005 — Outcome indicator per programme."""
    _name        = 'wamacare.indicator'
    _description = 'WamaCare Outcome Indicator'
    _order       = 'programme_id, sequence'
    _inherit     = ['mail.thread']

    name = fields.Char(string='Indicator', required=True, tracking=True,
                       help='e.g. "ANC visits completed", "Women trained", "Children immunised"')
    sequence     = fields.Integer(default=10)
    programme_id = fields.Many2one('project.project', string='Programme',
                                   required=True, ondelete='cascade')
    indicator_type = fields.Selection([
        ('count',      'Count (number)'),
        ('percentage', 'Percentage (%)'),
        ('amount',     'Amount (₦)'),
        ('yes_no',     'Yes / No'),
    ], string='Type', default='count', required=True)

    unit = fields.Char(string='Unit', help='e.g. beneficiaries, visits, sessions, %')

    # ── Targets ──────────────────────────────────────────────
    baseline     = fields.Float(string='Baseline', digits=(16, 2),
                                help='Starting value before programme began')
    target_value = fields.Float(string='Target', digits=(16, 2),
                                help='What we aim to achieve this period', tracking=True)
    current_value = fields.Float(string='Achieved', digits=(16, 2),
                                 tracking=True,
                                 help='Current value — update regularly from field data')
    progress_pct  = fields.Float(string='Progress %', compute='_compute_progress',
                                 store=True, digits=(5, 1))

    status = fields.Selection([
        ('on_track',  'On Track'),
        ('at_risk',   'At Risk'),
        ('off_track', 'Off Track'),
        ('achieved',  'Achieved'),
        ('not_started', 'Not Started'),
    ], string='Status', compute='_compute_status', store=True, tracking=True)

    # ── Period ───────────────────────────────────────────────
    date_from     = fields.Date(string='Period From')
    date_to       = fields.Date(string='Period To')
    frequency     = fields.Selection([
        ('monthly',    'Monthly'),
        ('quarterly',  'Quarterly'),
        ('annual',     'Annual'),
        ('once',       'One-off'),
    ], string='Reporting Frequency', default='quarterly')

    responsible_id = fields.Many2one('hr.employee', string='Responsible')
    notes          = fields.Text(string='Notes / Evidence')

    @api.depends('current_value', 'target_value')
    def _compute_progress(self):
        for rec in self:
            if rec.target_value:
                rec.progress_pct = (rec.current_value / rec.target_value) * 100
            else:
                rec.progress_pct = 0.0

    @api.depends('progress_pct', 'target_value', 'current_value')
    def _compute_status(self):
        for rec in self:
            if not rec.target_value:
                rec.status = 'not_started'
            elif rec.current_value >= rec.target_value:
                rec.status = 'achieved'
            elif rec.progress_pct >= 75:
                rec.status = 'on_track'
            elif rec.progress_pct >= 40:
                rec.status = 'at_risk'
            else:
                rec.status = 'off_track'
