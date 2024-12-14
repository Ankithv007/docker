from odoo import models, fields

class CustomModel(models.Model):
    _name = 'custom.module'  # Model identifier
    _description = 'Custom Module Example'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
