{
    'name': 'Custom Purchase Order',
    'version': '17.0.0.0',
    'summary': 'Customizes the purchase order report',
    'description': """
        This module customizes the purchase order report template
        to match a specific design requirement.
    """,
    'category': 'Purchases',
    'author': 'Your Name or Company',
    'website': 'https://www.yourwebsite.com',
    'license': 'LGPL-3',
    'depends': ['purchase'],
    'data': [
        'views/custom_report_purchaseorder.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}