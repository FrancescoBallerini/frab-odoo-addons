{
    "name": "Partner Default Pricelist (Website)",
    "version": "14.0.0.0.1",
    "summary": """
        Set default pricelist for e-commerce customers.
    """,
    "depends": ["website", "sale"],
    "author": "Francesco Ballerini",
    "data": [
        "views/website_views.xml",
        "views/res_config_settings.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
