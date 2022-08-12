# -*- coding: utf-8 -*-
###############################################################################
# MIT License
#
# Copyright (c) 2022 Monema S.r.l.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###############################################################################
{
    'name': 'Cookie Consent Klaro Integration',
    'summary': 'Cookie Consent Klaro Integration',
    'version': '14.0.1.1.0',

    'description': """
Cookie Consent Klaro Integration.
==============================================


    """,

    'author': 'Monema S.r.l.',
    'maintainer': 'Andrea Bettarini',
    'contributors': ['Andrea Bettarini <bettarini@monema.it>'],

    'website': 'https://monema.it/',

    'license': 'Other OSI approved licence',
    'category': 'Uncategorized',

    'depends': [
        'base',
        'website',
        'website_smartbuttons'
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
