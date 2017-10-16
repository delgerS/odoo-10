
from odoo import models, fields, api

class CustomSalesDashboard(models.Model):
    _name = 'custom.dashboard'
 
    # @api.one
    # def _get_count(self):
    #     quotations_count = self.env['todo.task'].search(
    #         [('stage_id', '=', 'Low')])
    #     orders_count = self.env['sale.order'].search(
    #         [('stage_id', '=', 'Low')])
    #     orders_done_count = self.env['sale.order'].search(
    #         [('stage_id', '=', 'Low')])
 
    #     self.orders_count = len(orders_count)
    #     self.quotations_count = len(quotations_count)
    #     self.orders_done_count = len(orders_done_count)
 
    color = fields.Integer(string='Color Index')
    name = fields.Char(string="Name")
    # orders_count = fields.Integer()
    quotations_count = fields.Integer()
    orders_done_count = fields.Integer()