{
    'name': 'Custom Module',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'A custom Odoo module for specific functionality.',
    'author': 'Ankith B V',
    'website': 'https://your-website.com',
    'depends': ['base'],  # Add other modules like 'sale', 'account', etc., if needed.
    'data': [
        'views/my_model_views.xml',  # Include your XML views.
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
