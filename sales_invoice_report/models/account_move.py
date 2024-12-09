from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    sales_amount_in_words = fields.Text(string='Amount In Words', compute='_compute_total_sales_amount_in_words')
    sale_order_id = fields.Many2one('sale.order', compute='_compute_sale_order', store=True)

    @api.depends('invoice_line_ids.sale_line_ids.order_id')
    def _compute_sale_order(self):
        for rec in self:
            rec.sale_order_id = rec.mapped('invoice_line_ids.sale_line_ids.order_id')

    # @api.depends('amount_total', 'currency_id')
    # def _compute_total_sales_amount_in_words(self):
    #     QAR = self.env['res.currency'].search([('name', '=', 'QAR')])
    #     if self.amount_total:
    #         sales_amount_in_words = QAR.amount_to_text(self.amount_total)
    #         sales_amount_in_words = sales_amount_in_words.replace("Rial", "Qatar Riyals only")
    #         self.sales_amount_in_words = sales_amount_in_words
    #     else:
    #         self.sales_amount_in_words = False

    @api.depends('amount_total', 'currency_id')
    def _compute_total_sales_amount_in_words(self):
        for move in self:
            if move.amount_total:
                move.sales_amount_in_words = move.currency_id.amount_to_text(move.amount_total)
            else:
                move.sales_amount_in_words = False