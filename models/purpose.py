# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import re

class KlaroPurpose(models.Model):
    _name = 'klaro.purpose'
    _description = 'Klaro Purpose'

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
        translate=True
    )
    description = fields.Text(
        string='description',
        translate=True
    )

    @api.constrains('name')
    def _check_name(self): 
        for record in self: 
            # checking if regular expression find any ' '(space) in name string then it will return False
            has_space = re.compile(' ').search(record.name)
            if has_space:
                raise ValidationError(_("The name cannot contains spaces, allowed characters are: [a-z,A-Z,0-9,'-','_']"))
