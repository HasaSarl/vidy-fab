from odoo import models, fields, api

class account_invoice(models.Model):
	_name = 'account.invoice'
	_inherit = ['account.invoice', 'ir.needaction_mixin']

	_defaults = {
		'partner_bank_id': 2,
	}
