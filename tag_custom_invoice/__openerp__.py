{
    'name': "Custom Invoices(TAGSBM)",
    'version': "1.1",
    'author': "TAGSBM",
    'category': "Tools",
    'summary': "Modifies invoice to display",
    'data': [
        'ir.ui.view.csv',
        'res_company.xml',
    ],
    'demo': [],
    'currrency':'EUR',
    'price': 4.99,
    'images':[
    'static/description/1.jpg',
    ],
    'depends': ['web', 'account','report'],
    'installable': True,
}