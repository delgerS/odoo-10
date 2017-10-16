
# -*- coding: utf-8 -*-

import socket
import fcntl
import struct
import firstconfig
import os
import re
from odoo import models, fields, api
class TodoTask(models.Model):
	""" TodoTask form main class """
	_name = 'todo.task'

	_rec_name='sequence_id'
	
	name 		=fields.Char('name')
	lname 		=fields.Char(string='last_name')
	username	=fields.Char('Username',required=True)
	valid_password 	=fields.Char('Password',required=True)
	email 		=fields.Char('Email',required=True)
	is_done 	=fields.Boolean('Done?')
	subtotal 	=fields.Integer()
	rec_name	=fields.Integer()
	product_ids	=fields.One2many('todo.tree','partent_id')
	sequence_id =fields.Char(string='Sequence ID',readonly=True)
	name 		=fields.Char(String='Description')
	color 		=fields.Char(string="Color")
	image 		=fields.Binary(string="image")
	stage_id 	=fields.Selection([('a','Low'),('b','Normal'),('c','High')],default='a')


	@api.model
	def install(self):
		""" when module insatll run terminal command in it"""
		os.system('sudo apt-get update')
		sudoPassword = 'odoo'
		command='sudo apt-get install python-mechanize'
		p = os.system('echo %s| sudo -S %s' % (sudoPassword, command))


	@api.onchange('username')
	def valid_user(self):
		""" validation username """
		if self.username:
			if len(str(self.username))>5:
				
				if not re.match("^[a-zA-Z 0-9_.-//s]*$", str(self.username)):
					self.username=""
					return {'value':{},'warning':{'title':
					'warning','message':"username Cantain only Char OR NUMBER e:g abc123"}}
				else:
					print "ooooooooooooo"
					if self.username.find(' '):
						print "aaaaaaa"
						return {'value':{},'warning':{'title':
								'warning','message':"username Cantain space enter valide username"}}
					else:
						username_search_record=self.env['todo.task'].search([['username', '=', self.username]])
						
						if len(username_search_record)>0:
							self.username=""
							return {'value':{},'warning':{'title':
							'warning','message':"username already register in db"}}
						else:
							pass
			else:
				self.username=""
				return {'value':{},'warning':{'title':
						'warning','message':"minimum leght is 6"}}

	
	@api.onchange('valid_password')
	def check_password1(self):
		""" validation password """
		if self.valid_password:
			
			if len(str(self.valid_password))>5:
				if not re.match('\d.*[A-Z]|[A-Z].*\d', str(self.valid_password)):
					return {'value':{},'warning':{'title':
					'warning','message':"Your password contain 1 upercase and and one number"}}
				else:
					pass
			else:
				self.valid_password=""
				return {'value':{},'warning':{'title':
					'warning','message':"minimum leght is 6"}}


	@api.onchange('email')
	def check_email1(self):
		""" validation email """
		if self.email:
			if len(str(self.email))>5:
				
				if not re.match('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$', str(self.email)):
					self.email=""
					return {'value':{},'warning':{'title':
					'warning','message':"invalid Email "+self.email+" type e:g abc@xyz.com"}}
				else:
					domain=self.email.split("@",1)[1]
					str2= ".."
					valid_email123=domain.find(str2)
					print valid_email123
					
					if valid_email123>0:
						self.email=""
						return {'value':{},'warning':{'title':
						'warning','message':"invalid Email "+self.email+" type e:g abc@xyz.com"}}
					else:
						pass
					
			else:
				self.email=""
				return {'value':{},'warning':{'title':
					'warning','message':"minimum leght is 6"}}


	@api.model
	def create(self, vals):
		""" sequence_id work perform  """
		vals['sequence_id'] = self.env['ir.sequence'].get('yasir.sgd')
		seq_return=super(TodoTask, self).create(vals)
		return seq_return

	# @api.multi
	# def write(self,val):

	# 	# val['name'] = "rauf"
	# 	record1122=super(TodoTask, self).write(val)
	# 	return record1122


	@api.multi
	def do_toggle_done(self):
		""" function receive the dictionary data from firstconfig.py file 
			and use in this function   """
		ip=self.get_ip_address('wlp8s0')
		url=firstconfig.truck['http']+str(ip)+firstconfig.truck['port']
		return {
			'name'     : 'Go to website',
			'res_model': 'ir.actions.act_url',
			'type'     : 'ir.actions.act_url',
			'target'   : 'current',	
			'url'		: url,
		}
	
	def get_ip_address(self, ifname):
		""" this function get the ip adress and
			 use ip adress do_toggle_done function """
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		return socket.inet_ntoa(fcntl.ioctl(
			s.fileno(),
			0x8915,  # SIOCGIFADDR
			struct.pack('256s', ifname[:15])
		)[20:24])


	@api.onchange('name','lname')
	def match(self):
		""" check name and lname field are equall if equal show warning masg  """
		if self.name==self.lname==0:
			pass
		elif self.name==self.lname:
			return {'value':{},'warning':{'title':
			'warning','message':"Your Name = "+ self.name + " AND Lname= "+ self.lname + " Are Same"}}
		else:
			pass

	@api.onchange('subtotal')
	def positive(self):
		""" function should subtotla field are always positive """
		if self.subtotal==0:
			self.subtotal=0
		else:
			self.subtotal=abs(self.subtotal)


class TodoTask_tree(models.Model):
	""" Tree class of  TodoTask class """
	_name='todo.tree'

	product 	=fields.Char()
	description	=fields.Text()
	date 		=fields.Date(string='date')
	quality		=fields.Float()
	unit_price	=fields.Float()
	subtotal	=fields.Integer()
	partent_id 	=fields.Many2one('todo.task')


class TodoTask_purchase_order(models.Model):
	""" class inherite purchas.order and get the data 
		tree or form and put the data tree or form in class todo.task  """
	_inherit='purchase.order'

	@api.model
	def create(self,val):
		record = super(TodoTask_purchase_order, self).create(val)
		todoTask_new=self.env['todo.task']
		new_record_create_id=todoTask_new.create({
			'name' : record.partner_id.id,
			})
		record_list=[]
		for x in record.order_line:
			lines=todoTask_new.product_ids.create({
			'product'		:x.product_id.id,
			'description'	:x.name,
			'date'			:x.date_planned,
			'quality'		:x.product_qty,
			'unit_price'	:x.price_unit,
			'subtotal'		:x.price_subtotal,
			'partent_id'	:new_record_create_id.id,
			})
		return record