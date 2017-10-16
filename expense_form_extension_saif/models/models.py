# -*- coding: utf-8 -*-

from odoo import models, fields, api
class test2(models.Model):
	""" MAin FOrm class  """
	_name	='saif.extension'

	Employee 	=fields.Char(string="Employee")
	date 		=fields.Date(string='Date')
	department	=fields.Char(string="Department")
	amount 		=fields.Integer(string='Amount')
	returned 	=fields.Float(string='Returned')
	net 		=fields.Float(string='Net')
	payment_bank=fields.Boolean(string='Toggle button(change)')
	cash_book	=fields.Char(string='Cash Book')
	description	=fields.Char(string='Description')
	curency	 	=fields.Char(string='Currency')
	typea	 	=fields.Char(string='Type')
	hide_F	 	=fields.Selection([('Employee','Employee'),('Date','Date'),
								 ('tree','tree')])
	state   	=fields.Selection([('a','stage1'),('b','stage2')],default='a')
	saif_tree_link= fields.One2many('saif.ext.tree','part_id')

		
	@api.onchange('saif_tree_link')
	def total_price(self):
		""" value assign tree field(saif_tree_link) to form in field(amount)  """
		self.amount=0
		for x in self.saif_tree_link:
			self.amount=self.amount+x.total


	@api.onchange('department')
	def capital(self):
		""" capitilized the department field using title() """
		if self.department:
			self.department =  str(self.department).title()


	@api.multi
	def change(self):
		""" click the button change and change the position od satage a or b """
		if self.state =='a':
			self.state='b'
		else:
			self.state='a'

	
	@api.multi
	@api.onchange('state')
	def change(self):
		if self.state=='b':
			return {'value':{},'warning':{'title':
			'warning','message':"You are enter the stage2"}}


class saif_extension_tree(models.Model):
	""" tree class """
	_name='saif.ext.tree'

	expense_date =fields.Date(string='Expense Date')
	expense_note=fields.Char(string='Expense Note')
	reference=fields.Char(string='Reference')
	unit_of_measure=fields.Char(string='Unit Of Measure')
	unit_of_price=fields.Integer(string='Unit Of Price')
	quantities=fields.Integer(string='Quantities')
	total=fields.Integer(string='Total')
	part_id =fields.Many2one('saif.extension')