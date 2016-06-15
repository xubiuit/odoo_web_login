# -*- encoding: utf-8 -*-
##############################################################################
#
#    Samples module for Odoo Web Login Screen
#    Copyright (C) 2016- XUBI.ME (http://www.xubi.me)
#    @author binhnguyenxuan (https://www.linkedin.com/in/binh-nguyen-xuan-46556279)
#
#    This program is paid software base on OEEL-1 license
#    
#    Background Source: http://forum.xda-developers.com/showpost.php?p=37322378
#
##############################################################################
{
    'name': 'Odoo Web Login Screen',
    'summary': 'The new configurable Odoo Web Login Screen',
    'version': '9.0.1.0.0',
    'category': 'Website',
    'summary': """
The new configurable Odoo Web Login Screen
""",
    'author': "binhnguyenxuan (https://www.linkedin.com/in/binh-nguyen-xuan-46556279)",
    'website': 'http://www.xubi.me',
    'license': 'OEEL-1',
    'depends': [
    ],
    'data': [
        'data/ir_config_parameter.xml',
        'templates/webclient_templates.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'price': 11.00,
    'currency': 'EUR',
}
