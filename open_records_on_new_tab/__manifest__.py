# -*- coding: utf-8 -*-
{
    'name': "Open Records on New Tab",
    'summary': """
        Open list view records in a new browser tab with Ctrl+Click or Middle-Click""",
    'description': """
        This module enhances the Odoo list view functionality by allowing users
        to open records in a new browser tab using multiple methods.
        Features:
        - Ctrl+Click (or Cmd+Click on Mac) on any list view record to open it in a new tab
        - Middle-Click (mouse wheel click) on any list view record to open it in a new tab
        - Normal click behavior remains unchanged
        - Works on all list views and kanban views throughout Odoo
        - Preserves the current menu context when opening in new tab
    """,
    'author': "Francesco Ballerini",
    'website': "https://github.com/FrancescoBallerini",
    'category': 'Tools',
    'version': '14.0.0.0.4',
    'license': 'LGPL-3',

    'depends': ['base', 'web'],
    'data': [
        'views/assets.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
