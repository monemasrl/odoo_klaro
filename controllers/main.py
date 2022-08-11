# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo.http import route, request, Response, Controller
from odoo.exceptions import UserError, ValidationError
import json

class ControllerName(Controller):
    """ The summary line for a class docstring should fit on one line.

        Routes:
          /some_url: url description
    """
    @route('/klaro/config.js', type='http', auth='none', website=True)
    def klaroConfig(self, **kw):
        headers = {"Content-Type": "application/json"}

        parameters = request.env['ir.config_parameter'].sudo()
        klaro_testing =  parameters.get_param('klaro.testing')
        klaro_element_id =  parameters.get_param('klaro.element_id')
        klaro_storage_method =  parameters.get_param('klaro.storage_method')
        klaro_storage_name =  parameters.get_param('klaro.storage_name')
        klaro_html_texts =  parameters.get_param('klaro.html_texts')
        klaro_cookie_domain =  parameters.get_param('klaro.cookie_domain')
        klaro_expires_after_days =  parameters.get_param('klaro.expires_after_days')
        klaro_default =  parameters.get_param('klaro.default')
        klaro_must_consent =  parameters.get_param('klaro.must_consent')
        klaro_accept_all =  parameters.get_param('klaro.accept_all')
        klaro_hide_decline_all =  parameters.get_param('klaro.hide_decline_all')
        klaro_hide_learn_more =  parameters.get_param('klaro.hide_learn_more')
        klaroConfig = {
            "testing": klaro_testing,
            "elementID": klaro_element_id,
            "storageMethod": klaro_storage_method,
            "storageName": klaro_storage_name,
            "htmlTexts": klaro_html_texts,
            "cookieDomain": klaro_cookie_domain,
            "cookieExpiresAfterDays": klaro_expires_after_days,
            "default": klaro_default,
            "mustConsent": klaro_must_consent,
            "acceptAll": klaro_accept_all,
            "hideDeclineAll": klaro_hide_decline_all,
            "hideLearnMore": klaro_hide_learn_more
        }

        klaroConfig['services'] = []
        klaroConfig['services'].append({
            "name": 'youtube',
            "contextualConsentOnly": True,
        })

        return Response(json.dumps(klaroConfig, indent=4), headers=headers)
        # services: [
        #     {
        #         name: 'matomo',
        #         default: true,
        #         purposes: ['analytics'],

        #         cookies: [
        #             [/^_pk_.*$/, '/', 'klaro.kiprotect.com'],
        #             [/^_pk_.*$/, '/', 'localhost'],
        #             'piwik_ignore',
        #         ],
        #         callback: function(consent, service) {
        #             console.log(
        #                 'User consent for service ' + service.name + ': consent=' + consent
        #             );
        #         },
        #         required: false,
        #         optOut: false,
        #         onlyOnce: true,
        #     },

        # ],

