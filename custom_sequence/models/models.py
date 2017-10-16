# -*- coding: utf-8 -*- 
from openerp import models, fields, api, _
from openerp.exceptions import UserError, ValidationError, Warning
class cashadvance(models.Model):
	_name = 'comben.cashadvance'
	
	sequence_id =fields.Char(string='Sequence ID')

	@api.model
	def create(self, vals):
		vals['sequence_id'] = self.env['ir.sequence'].get('comben.cashadvance')
		return super(cashadvance, self).create(vals)