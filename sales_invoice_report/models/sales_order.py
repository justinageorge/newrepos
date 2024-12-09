from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contact_name = fields.Char(string='Contact Name', readonly=False)
    rfq_no = fields.Char(String='RFQ No')
    other_ref = fields.Char(string='Other Ref')
    po_number = fields.Char(string='Purchase Order No.')
    po_reference = fields.Char(string='Other Reference')
