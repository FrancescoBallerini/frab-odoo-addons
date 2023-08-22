#  Copyright 2023 Francesco Ballerini
#  License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Pricelist Percent Change Supplier Info",
    "version": "14.0.0.0.1",
    "category": "Product",
    "summary": """
        Enable, on pricelist views, percentage change computation and
        price simulation, for rules based on supplierinfo prices (only 
        for rules applied at product level). """,
    "author": "Francesco Ballerini",
    "support": "francescobl.lavoro@gmail.com",
    "depends": [
        "product_form_pricelist_percent_change",
        "product_pricelist_supplierinfo",
    ],
    "data": [],
    "application": False,
    "installable": True,
    "license": "AGPL-3",
}
