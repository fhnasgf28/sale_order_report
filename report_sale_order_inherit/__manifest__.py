{
    'name': "Report Sale Order Inherit",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'stock', 'purchase','sale_management', 'sale_order_inherit'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        # "views/sale_report_booking_order_pivot.xml",
        "report/report_booking_order_customer.xml",
        "views/booking_order_pivot_views.xml",
        "views/menus.xml",

    ],
    'installable': True,
    'application': True,
}
# -*- coding: utf-8 -*-
