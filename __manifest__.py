{
    'name': 'Custom Delivery Note',
    'version': '17.0.1.0',
    'category': 'Inventory',
    'summary': 'Customized delivery note for Odoo 17',
    'depends': ['stock', 'sale'],
    'data': [
        'views/stock_picking_views.xml',
        'report/delivery_note_report.xml',
        'data/ir_sequence_data.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}