# -*- coding: utf-8 -*- 

from openerp import models, fields, api, _
# from openerp.exceptions import UserError, ValidationError, Warning

class call_customer(models.Model):
	_inherit = 'res.partner'

	@api.multi
	def call(self):
		print "ssssssssssssssssss"
