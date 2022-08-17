###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class Website(models.Model):
    _inherit = "website"

    @api.multi
    def edit_klaro_config(self):
        config_id = self.env["klaro.website"].search([("website_id", "=", self.id)])
        action = {
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "klaro.website",
            "view_id": self.env.ref("klaro.view_klaro_website_form").id,
            "context": {"default_website_id": self.id},
            "target": "current",
        }

        if config_id:
            action.update({"res_id": config_id.id})

        return action

    @api.multi
    def get_klaro_config(self):
        KlaroWebsiteModel = self.env["klaro.website"]
        klaro_website_id = KlaroWebsiteModel.search([("website_id", "=", self.id)])

        if klaro_website_id:
            return klaro_website_id.get_klaro_config()
        else:
            return {}


class KlaroWebsite(models.Model):
    _name = "klaro.website"
    _inherits = {"website": "website_id"}

    website_id = fields.Many2one(
        string="website", comodel_name="website", ondelete="cascade", required=True
    )

    klaro_title = fields.Char(
        string="Title", help="""Modal title""", translate=True, required=True
    )

    klaro_testing = fields.Boolean(
        string="Testing",
        help="""Setting 'testing' to 'true' will cause Klaro to not show the consent notice or
    modal by default, except if a special hash tag is appended to the URL (#klaro-
    testing). This makes it possible to test Klaro on your live website without
    affecting normal visitors.""",
        default=True,
    )

    klaro_disable_powered_by = fields.Boolean(
        string='Powered by "Klaro"',
        help="""You can also remove the 'Realized with Klaro!' text in the consent modal.
    Please don't do this! We provide Klaro as a free open source tool.
    Placing a link to our website helps us spread the word about it,
    which ultimately enables us to make Klaro! better for everyone.
    So please be fair and keep the link enabled. Thanks :)""",
        default=False,
    )

    klaro_additional_class = fields.Char(
        string="Additional Class",
        help="""you can specify an additional class (or classes) that will be added to the
    Klaro `div`""",
    )

    klaro_element_id = fields.Char(
        string="Element Id",
        help="""You can customize the ID of the DIV element that Klaro will create when starting
    up. By default, Klaro will use 'klaro'.""",
        default="klaro",
    )

    klaro_storage_method = fields.Selection(
        string="Storage Method",
        selection=[("cookie", "cookie"), ("localStorage", "localStorage")],
        help="""You can customize how Klaro persists consent information in the browser. Specify
    either cookie' (the default) or 'localStorage'.""",
        default="cookie",
    )

    klaro_storage_name = fields.Char(
        string="Storage Name",
        help="""You can customize the name of the cookie or localStorage entry that Klaro will
    use for storing the consent information. By default, Klaro will use 'klaro'.""",
        default="klaro",
    )

    klaro_html_text = fields.Boolean(
        string="Html Text",
        help="""If set to `true`, Klaro will render the texts given in the
    `consentModal.description` and `consentNotice.description` translations as HTML.
    This enables you to e.g. add custom links or interactive content.""",
        default=False,
    )

    klaro_cookie_domain = fields.Char(
        string="Cookie Domain",
        help="""You can change the cookie domain for the consent manager itself. Use this if you
    want to get consent once for multiple matching domains. By default, Klaro will
    use the current domain. Only relevant if 'storageMethod' is set to 'cookie'.""",
    )

    klaro_cookie_path = fields.Char(
        string="Cookie Path",
        help="""You can change to cookie path for the consent manager itself.
    Use this to restrict the cookie visibility to a specific path.
    If undefined, Klaro will use '/' as cookie path.""",
        default="/",
    )

    klaro_expires_after_days = fields.Integer(
        string="Expires After Days",
        help="""You can also set a custom expiration time for the Klaro cookie. By default, it
    will expire after 30 days. Only relevant if 'storageMethod' is set to 'cookie'.""",
        default=365,
    )

    klaro_default = fields.Boolean(
        string="Default",
        help="""Defines the default state for services in the consent modal (true=enabled by
    default). You can override this setting in each service.""",
        default=False,
    )

    klaro_must_consent = fields.Boolean(
        string="Must Consent",
        help="""If 'mustConsent' is set to 'true', Klaro will directly display the consent
    manager modal and not allow the user to close it before having actively
    consented or declined the use of third-party services.""",
        default=True,
    )

    klaro_accept_all = fields.Boolean(
        string="Accept All",
        help="""Setting 'acceptAll' to 'true' will show an "accept all" button in the notice and
    modal, which will enable all third-party services if the user clicks on it. If
    set to 'false', there will be an "accept" button that will only enable the
    services that are enabled in the consent modal.""",
        default=True,
    )

    klaro_hide_decline_all = fields.Boolean(
        string="Hide Decline All",
        help="""Setting 'hideDeclineAll' to 'true' will hide the "decline" button in the consent
    modal and force the user to open the modal in order to change his/her consent or
    disable all third-party services. We strongly advise you to not use this
    feature, as it opposes the "privacy by default" and "privacy by design"
    principles of the GDPR (but might be acceptable in other legislations such as
    under the CCPA)""",
        default=False,
    )

    klaro_hide_learn_more = fields.Boolean(
        string="Hide Learn More",
        help="""Setting 'hideLearnMore' to 'true' will hide the "learn more / customize" link in
    the consent notice. We strongly advise against using this under most
    circumstances, as it keeps the user from customizing his/her consent choices.""",
        default=False,
    )

    klaro_service_ids = fields.Many2many(
        string="service",
        comodel_name="klaro.service",
        relation="klaro_service_klaro_website_rel",
        column2="klaro_service_id",
        column1="klaro_website_id",
    )

    klaro_privacy_policy_url = fields.Char(
        string="Privacy Policy URL", required=True, translate=True, default="/privacy"
    )

    klaro_consent_notice_description = fields.Html(
        string="Notice Description",
        required=True,
        translate=True,
        default="Default Consent Notice Description",
    )

    klaro_consent_modal_description = fields.Html(
        string="Modal Description",
        required=True,
        translate=True,
        default="Default Consent Modal Description",
    )

    klaro_embedded = fields.Boolean(string="Embedded", default=False)
    klaro_notice_as_modal = fields.Boolean(string="Notice as modal", default=False)
    klaro_no_autoload = fields.Boolean(string="No autoload", readonly=False)

    klaro_group_by_purpose = fields.Boolean(string="Group by purpose", default=True)

    klaro_vertical_position = fields.Selection(
        [("top", "Top"), ("bottom", "Bottom")],
        string="Vertical Position",
        default="bottom",
    )

    klaro_horizontal_position = fields.Selection(
        [("left", "Left"), ("right", "Right")],
        string="Horizontal Position",
        default="right",
    )

    klaro_wide = fields.Boolean(string="Wide", default=False)

    klaro_theme_light = fields.Boolean(string="Light Theme", default=True)

    klaro_watch_enabled = fields.Boolean(
        string="Watch enabled",
    )

    klaro_watch_function = fields.Text(
        string="Watch Function",
    )

    def get_klaro_config(self):
        lang = self.env.user.lang.split("_")[0]
        klaro_config = {
            "version": 1,
            "title": self.klaro_title,
            "elementID": self.klaro_element_id,
            "styling": {
                "theme": ["light", "top", "wide"],
            },
            "noAutoLoad": self.klaro_no_autoload,
            "htmlTexts": self.klaro_html_text,
            "embedded": self.klaro_embedded,
            "groupByPurpose": self.klaro_group_by_purpose,
            "storageMethod": self.klaro_storage_method,
            "cookieName": self.klaro_storage_name,
            "cookieExpiresAfterDays": self.klaro_expires_after_days,
            "cookieDomain": self.klaro_cookie_domain,
            "cookiePath": self.klaro_cookie_path,
            "default": self.klaro_default,
            "mustConsent": self.klaro_must_consent,
            "acceptAll": self.klaro_accept_all,
            "hideDeclineAll": self.klaro_hide_decline_all,
            "hideLearnMore": self.klaro_hide_learn_more,
            "noticeAsModal": self.klaro_notice_as_modal,
            "disablePoweredBy": self.klaro_disable_powered_by,
            "additionalClass": self.klaro_additional_class,
            "privacyPolicyUrl": self.klaro_privacy_policy_url,
            "consentNoticeDescription": self.klaro_consent_notice_description,
            "consentModalDescription": self.klaro_consent_modal_description,
            "watchEnabled": self.klaro_watch_enabled,
            "watchFunction": self.klaro_watch_function,
            "lang": lang,
        }
        klaro_config["styling"] = []

        klaro_config["styling"].append(self.klaro_horizontal_position)
        klaro_config["styling"].append(self.klaro_vertical_position)

        if self.klaro_theme_light:
            klaro_config["styling"].append("light")

        if self.klaro_wide:
            klaro_config["styling"].append("wide")

        klaro_config["services"] = []
        klaro_config["purposes"] = []

        for service in self.klaro_service_ids:
            service_purposes = []
            for purpose in service.purpose_ids:
                service_purposes.append(purpose.name)
            service_config = {"name": service.name, "purposes": service_purposes}
            if service.title:
                service_config.update({"title": service.title})
            if service.description:
                service_config.update({"description": service.description})
            if service.contextual_consent_only:
                service_config.update({"contextualConsentOnly": True})
            if service.on_init:
                service_config.update({"onInit": service.on_init})
            if service.on_accept:
                service_config.update({"onAccept": service.on_accept})
            if service.on_decline:
                service_config.update({"onDecline": service.on_decline})
            if service.only_once:
                service_config.update({"onlyOnce": True})
            if service.required:
                service_config.update({"required": True})
            if service.opt_out:
                service_config.update({"optOut": True})
            if service.vars:
                service_config.update({"vars": service.vars})
            if service.cookies:
                service_config.update({"cookies": service.cookies})
            klaro_config["services"].append(service_config)
            _logger.debug("Service Config: {}".format(service_config))

        PurposeModel = self.env["klaro.purpose"].sudo()

        purposes = PurposeModel.search([])

        for purpose in purposes:
            purpose_config = {
                "name": purpose.name,
                "title": purpose.title,
                "description": purpose.description,
            }
            klaro_config["purposes"].append(purpose_config)
        _logger.debug("Klaro Config: {}".format(klaro_config))

        return klaro_config
