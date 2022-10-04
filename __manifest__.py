# -*- coding: utf-8 -*-
# SilkSoft.org Module.

{
    'name': 'SilkSoft Form Management',
    'version': '15.0.1.0.0',
    'category': 'Productivity/Forms',
    'summary': 'Demo module for Sukari Gold Mine management',
    'sequence': '5',
    'author': 'Amr Salama',
    'license': 'LGPL-3',
    'company': 'SilkSoft',
    'maintainer': 'SilkSoft',
    'support': 'To Be Added',
    'website': 'https://silksoft.org',
    'depends': ['hr'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/observation_form.xml',
        'views/menu_items.xml',
        'views/reports.xml',
        'views/observation_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/icon.png'],
    'qweb': [],
}
