{
    "name": "Website Sale: Sort By Pricelist Price",
    "version": "14.0.0.0.1",
    "depends": ["website_sale", "product_sort_by_price_base"],
    "author": "Francesco Ballerini",
    "description": """
        Compatibility between e-Commerce Sort By and Pricelist Prices.
        At the moment this feature is only available for Product Templates.
    """,
    "data": [
        "views/assets.xml",
        "views/templates.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
