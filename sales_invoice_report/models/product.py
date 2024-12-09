from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_extra_charge = fields.Boolean(default=False)


