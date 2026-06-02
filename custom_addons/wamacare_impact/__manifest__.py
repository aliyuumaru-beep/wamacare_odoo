{
    'name': 'WamaCare Impact Measurement',
    'version': '17.0.1.0.0',
    'summary': 'Outcome indicators, cost-per-beneficiary, and programme KPI dashboard',
    'description': '''
Phase C — Impact Management
=============================
- ME-005: Outcome indicator definition and tracking per programme
- ME-006: Cost-per-beneficiary computed from analytic spend
- EXEC-004: Programme KPI dashboard
- EXEC-005: Beneficiary statistics per programme
    ''',
    'author': 'WamaCare (Tiko CBO)',
    'category': 'WamaCare/Impact',
    'depends': ['project', 'analytic', 'contacts', 'wamacare_safeguarding'],
    'data': [
        'security/ir.model.access.csv',
        'data/wamacare_indicator_sequence.xml',
        'views/wamacare_indicator_views.xml',
        'views/project_project_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
