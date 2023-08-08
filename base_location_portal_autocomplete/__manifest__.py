{
    'name': "Website Portal: Location Autocomplete",
    'version': '14.0.0.0.1',
    'depends': [
        'website',
        'portal',
        'base_location'
    ],
    'author': "Francesco Ballerini",
    'summary': """
        Enable auto-completion for Portal Address fields.
    """,
    'data': [
        'views/assets.xml',
        'views/portal_template_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
