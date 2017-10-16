# -*- coding: utf-8 -*-

from odoo import models, fields, api
class test2(models.Model):
	""" test2 model class tree and form field declare in one class """
	_name	='test2.test2'

	name 	 	=fields.Char('res.partner')
	lname	 	=fields.Char()
	Tax	 		=fields.Char()
	password   	=fields.Selection([('a','A')])
	product_ids	= fields.One2many('test2.test2','partent_id')
	product 	=fields.Char()
	description	=fields.Text()
	date 		=fields.Date(string='date')
	quality		=fields.Float()
	unit_price	=fields.Float()
	subtotal	=fields.Integer()
	partent_id 	=fields.Many2one('test2.test2')
	abc			=fields.Many2many('product.template',string='Many2many')
	xyz			=fields.Many2one('account.invoice',string='Many2one')

	

	@api.onchange('unit_price')
	def total_price(self):
		""" unite_price value assign to product both are tree value """
		self.product=self.unit_price
	

	
	
	@api.onchange('name','lname')
	def match(self):
		""" check name and lname field are equall if equal show warning masg  """
		if self.name==self.lname==0:
			pass
		elif self.name==self.lname:
			return {'value':{},'warning':{'title':
			'warning','message':"Your Name= "+ self.name + "OR Lname= "+ self.lname + "Are Same"}}
		else:
			pass

	

	@api.onchange('subtotal')
	def positive(self):
		""" function should subtotla field are always positive """
		if self.subtotal==0:
			self.subtotal=0
		else:
			self.subtotal=abs(self.subtotal)
	
	

	@api.multi
	def do_toggle_done(self):
		""" when click the togle button open the new form of model test2 """
		return {
		'name': 'My Window',
		'domain': [],
		'res_model': 'custom.wizard',
		'type'	   : 'ir.actions.act_window',
		'view_mode': 'form',
		'view_type': 'form',
		'context': {},
		'target': 'new',
	  }




# .......................test1 create work in purchase.order .........

# class abc(models.Model):
# 	""" this class inherite the purchase.order class """
# 	_inherit='purchase.order'


# 	@api.model
# 	def create(self, values):
# 		""" get the tree or form value of purchase.order put in model test2.test2 in tree"""
# 		record = super(abc, self).create(values)
# 		test2=self.env['test2.test2']
# 		# test4=self.env['test2.test2'].search([])
# 		print test2
# 		# print test4
# 		for x in record.order_line:
# 			new123=test2.create({
# 			'name' : record.partner_id.id
# 			})
# 			lines=test2.product_ids.create({
# 			'product'		:x.product_id.id,
# 			'description'	:x.name,
# 			'date'			:x.date_planned,
# 			'quality'		:x.product_qty,
# 			'unit_price'	:x.price_unit,
# 			'subtotal'		:x.price_subtotal,
# 			'partent_id'	:new123.id,
# 			})
# 		return record
