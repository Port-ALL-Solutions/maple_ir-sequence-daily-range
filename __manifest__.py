# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Daily Sequence',
    'category': '',
    'version': '1.0',
    'author': "Benoit Vézina & Pierre Dalpé pour Portall",
    'website': "portall.ca",
    'summary': 'Modification of Ir_Sequence for daily Sequence.',
    'description':
        """
Modification of Ir_Sequence for daily Sequence..
================================================

Modification of Ir_Sequence for daily Sequence..
        """,
    'depends': [
        'base',
    ],
    'data': [
        'views/ir_sequence_view.xml',
    ],
    'qweb': [
#        "static/src/xml/*.xml",
    ],
#    'bootstrap': True,  # load translations for login screen
    'installable': True,
    'application': False,
    'auto_install': False,
}

