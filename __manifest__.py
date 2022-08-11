# -*- coding: utf-8 -*-
###############################################################################
#
#    jeffery CHEN fan<jeffery9@gmail.com>
#
#    Copyright (c) All rights reserved:
#        (c) 2017  TM_FULLNAME
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
#    Odoo and OpenERP is trademark of Odoo S.A.
#
###############################################################################
{
    'name': 'Cookie Consent Klaro Integration',
    'summary': 'Cookie Consent Klaro Integration',
    'version': '1.0',

    'description': """
Cookie Consent Klaro Integration.
==============================================


    """,

    'author': 'Monema S.r.l.',
    'maintainer': 'Monema S.r.l.',
    'contributors': ['Monema S.r.l. <info@monema.it>'],

    'website': 'https://monema.it/',

    'license': 'AGPL-3',
    'category': 'Uncategorized',

    'depends': [
        'base',
        'website',
    ],
    'data': [
        'views/templates.xml',
        'views/assets.xml',
        'views/website_views.xml',
        'views/service_views.xml',
        'views/purpose_views.xml',
        'views/menu.xml',
        'views/snippets/consent_link.xml',
        'views/snippets/snippets.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True
}
