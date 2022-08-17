###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

import re

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class KlaroService(models.Model):
    _name = "klaro.service"
    _description = "Klaro Service"

    _rec_name = "name"
    _order = "name ASC"

    name = fields.Char(required=True, default=lambda self: _("New"), copy=False)

    title = fields.Char(copy=False, translate=True)

    description = fields.Text(translate=True)

    purpose_ids = fields.Many2many(
        string="purpose",
        comodel_name="klaro.purpose",
        relation="klaro_purpose_klaro_service_rel",
        column1="klaro_purpose_id",
        column2="klaro_service_id",
    )

    contextual_consent_only = fields.Boolean()

    on_accept = fields.Text()

    on_decline = fields.Text()

    on_init = fields.Text()

    cookies = fields.Text()

    vars = fields.Text()

    callback = fields.Text()

    required = fields.Boolean()

    opt_out = fields.Boolean(
        string="optOut",
    )

    only_once = fields.Boolean()

    @api.constrains("name")
    def _check_name(self):
        for record in self:
            # checking if regular expression find any ' '(space) in name string then
            # it will return False
            has_space = re.compile(" ").search(record.name)
            if has_space:
                raise ValidationError(
                    _(
                        "The name cannot contains spaces, "
                        "allowed characters are: [a-z,A-Z,0-9,'-','_']"
                    )
                )
