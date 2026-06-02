from odoo import models, fields, api


class ProjectProject(models.Model):
    """ME-006 cost-per-beneficiary + EXEC-005 beneficiary stats on programme."""
    _inherit = 'project.project'

    # ── Indicators ───────────────────────────────────────────
    x_indicator_ids = fields.One2many(
        'wamacare.indicator', 'programme_id', string='Outcome Indicators'
    )
    x_indicator_count = fields.Integer(
        compute='_compute_indicator_count', string='Indicators'
    )

    # ── EXEC-005 Beneficiary statistics ──────────────────────
    x_beneficiary_count = fields.Integer(
        string='Beneficiaries Served',
        help='Number of unique beneficiaries reached by this programme. Update from field data.',
        tracking=True,
    )
    x_target_beneficiaries = fields.Integer(
        string='Target Beneficiaries',
        help='How many beneficiaries are planned to be served this period.',
    )
    x_beneficiary_reach_pct = fields.Float(
        string='Reach %', compute='_compute_reach', store=True, digits=(5, 1)
    )

    # ── ME-006 Cost per beneficiary ───────────────────────────
    x_total_spend = fields.Float(
        string='Total Spend (₦)', compute='_compute_spend', store=False,
        help='Sum of all expenses charged to this programme\'s analytic account.'
    )
    x_cost_per_beneficiary = fields.Float(
        string='Cost per Beneficiary (₦)', compute='_compute_spend', store=False,
        digits=(16, 0),
        help='Total spend ÷ beneficiaries served'
    )

    @api.depends('x_indicator_ids')
    def _compute_indicator_count(self):
        for p in self:
            p.x_indicator_count = len(p.x_indicator_ids)

    @api.depends('x_beneficiary_count', 'x_target_beneficiaries')
    def _compute_reach(self):
        for p in self:
            if p.x_target_beneficiaries:
                p.x_beneficiary_reach_pct = (p.x_beneficiary_count / p.x_target_beneficiaries) * 100
            else:
                p.x_beneficiary_reach_pct = 0.0

    def _compute_spend(self):
        """ME-006: Sum analytic lines for this programme's account."""
        for p in self:
            analytic = p.analytic_account_id
            if analytic:
                lines = self.env['account.analytic.line'].search(
                    [('account_id', '=', analytic.id)]
                )
                total = sum(abs(l.amount) for l in lines)
                p.x_total_spend = total
                p.x_cost_per_beneficiary = (
                    total / p.x_beneficiary_count if p.x_beneficiary_count else 0.0
                )
            else:
                p.x_total_spend = 0.0
                p.x_cost_per_beneficiary = 0.0

    def action_view_indicators(self):
        self.ensure_one()
        return {
            'type':      'ir.actions.act_window',
            'name':      f'Indicators — {self.name}',
            'res_model': 'wamacare.indicator',
            'view_mode': 'list,form',
            'domain':    [('programme_id', '=', self.id)],
            'context':   {'default_programme_id': self.id},
        }
