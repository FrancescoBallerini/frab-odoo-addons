{
    "name": "Base Location Cities NUTS 3",
    "description": """ Add NUTS reference (level 3) on "Cities" records. """,
    "version": "14.0.0.0.1",
    "depends": [
        "base_location_nuts",
        "base_location",
    ],
    "author": "Francesco Ballerini",
    "category": "Partner Management",
    "data": [
        "security/ir.model.access.csv",
        "views/res_city_views.xml",
        "wizard/city_nuts3_sync_views.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
