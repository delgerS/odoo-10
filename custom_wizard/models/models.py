# -*- coding: utf-8 -*- 

from openerp import models, fields, api, _
# from openerp.exceptions import UserError, ValidationError, Warning


class CustomWizard(models.TransientModel):
    _name = "custom.wizard"

    name = fields.Char('Name', required=True)
    
    
    @api.multi
    def create_request(self):
    	""" custom_wizard value(name) assign to test1 model(todo.task) field name """
        abc=self.env['todo.task'].search([])
        for x in abc:
        	x.name = self.name