# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import re


class KlaroService(models.Model):
    _name = 'klaro.service'
    _description = 'Klaro Service'

    _rec_name = 'name'
    _order = 'name ASC'

    name = fields.Char(
        string='Name',
        required=True,
        default=lambda self: _('New'),
        copy=False
    )

    title = fields.Char(
        string='Title',
        copy=False,
        translate=True
    )

    description = fields.Text(
        string='Description',
        translate=True
    )

    purpose_ids = fields.Many2many(
        string='purpose',
        comodel_name='klaro.purpose',
        relation='klaro_purpose_klaro_service_rel',
        column1='klaro_purpose_id',
        column2='klaro_service_id',
    )

    contextual_consent_only = fields.Boolean(
        string='Contextual Consent Only',
    )

    on_accept = fields.Text(
        string='On Accept',
    )

    on_decline = fields.Text(
        string='On Decline',
    )

    on_init = fields.Text(
        string='On Init',
    )

    cookies = fields.Text(
        string='cookies',
    )

    vars = fields.Text(
        string='vars',
    )

    callback = fields.Text(
        string='Callback',
    )

    required = fields.Boolean(
        string='required',
    )

    opt_out = fields.Boolean(
        string='optOut',
    )

    only_once = fields.Boolean(
        string='Only Once',
    )

    @api.constrains('name')
    def _check_name(self): 
        for record in self: 
            # checking if regular expression find any ' '(space) in name string then it will return False
            has_space = re.compile(' ').search(record.name)
            if has_space:
                raise ValidationError(_("The name cannot contains spaces, allowed characters are: [a-z,A-Z,0-9,'-','_']"))
