from odoo import models, fields, api, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    fax_no = fields.Char(string='Fax No')
