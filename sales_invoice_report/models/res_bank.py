from odoo import models, fields, api, _


class ResBank(models.Model):
    _inherit = 'res.bank'

    bank_branch = fields.Char(string='Bank Branch')
    qar_acc_number = fields.Char(string='QAR Account Number')
    usd_acc_number = fields.Char(string='USD Account Number')
    swift_code = fields.Char(string='Swift Code')
    iban_qar = fields.Char(string='IBAN QAR')
    iban_usd = fields.Char(string='IBAN USD')
    account_name = fields.Char(string='Account Name')