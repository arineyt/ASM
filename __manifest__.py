{
    'name': "ASM",

    'summary': """
        Automotive Service Management""",

    'author': "Dmytro Stopchak",
    'category': 'Uncategorized',
    'version': '15.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/asm_groups.xml',
        'wizard/asm_confirm_order_views.xml',
        'security/asm.security.xml',
        'security/ir.model.access.csv',
        'views/asm_menus.xml',
        'views/asm_employee_views.xml',
        'views/asm_contact_person_views.xml',
        'views/asm_car_views.xml',
        'views/asm_order_views.xml',
        'views/asm_type_of_repair_views.xml',
        'data/asm_sequence_data.xml',
        'data/asm_type_repair_data.xml',
        'report/asm_managers_order_report.xml',
        'report/asm_managers_order_templates.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'data/asm_type_repair_data.xml',
        'data/asm_contact_person_data.xml',
        'data/asm_employee_data.xml',
        'data/asm_car_data.xml',
        'data/asm_order_data.xml',
        'data/asm_order_line_data.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
