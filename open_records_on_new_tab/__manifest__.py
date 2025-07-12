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
    'version': '16.0.1.0.0',
    'license': 'LGPL-3',

    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': [
            'open_records_on_new_tab/static/src/js/list_renderer.js',
            'open_records_on_new_tab/static/src/js/kanban_record.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
