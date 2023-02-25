#  Copyright 2023 Francesco Ballerini
#  License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Form Pricelist Percent Change",
    "version": "14.0.0.0.1",
    "category": "Product",
    "author": "Francesco Ballerini, Odoo Community Association (OCA)",
    "support": "francescobl.lavoro@gmail.com",
    "depends": [
        "product_form_pricelist",
    ],
    "data": [
        'views/product_template_view.xml',
        'views/product_pricelist_views.xml',
    ],
    "application": False,
    "installable": True,
    "license": "AGPL-3",
}
