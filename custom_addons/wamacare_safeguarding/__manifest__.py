{
    'name': 'WamaCare Safeguarding & Case Management',
    'version': '17.0.1.0.0',
    'summary': 'Beneficiary consent, case management, and safeguarding alerts for WamaCare NGO/CBO',
    'description': '''
Phase B — Beneficiary & Safeguarding
=====================================
- BEN-007: Beneficiary consent tracking (NDPR compliance)
- BEN-008: Structured case management per beneficiary
- BEN-009: Timestamped case notes
- SAFE-005: Safeguarding alert flags on beneficiary records
- SAFE-006: Case escalation workflow to Safeguarding Lead
- SAFE-007: Evidence upload and attachment to cases
- SAFE-008: Referral pathway tracking
    ''',
    'author': 'WamaCare (Tiko CBO)',
    'category': 'WamaCare/Safeguarding',
    'depends': ['contacts', 'mail', 'hr', 'project'],
    'data': [
        'security/wamacare_safeguarding_groups.xml',
        'security/ir.model.access.csv',
        'data/wamacare_case_sequence.xml',
        'views/wamacare_case_views.xml',
        'views/res_partner_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
