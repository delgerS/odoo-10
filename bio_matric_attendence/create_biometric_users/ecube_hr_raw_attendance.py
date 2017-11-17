from openerp import models, fields, api
from openerp.exceptions import Warning
from odoo.exceptions import UserError
from openerp.exceptions import UserError


class EcubeRawAttendance(models.Model):
	_name = 'ecube.raw.attendance'
	_description = 'EcubeRawAttendance'
	name = fields.Char('Machine Name')
	employee_id = fields.Many2one('hr.employee',string="Employee")
	attendance_date = fields.Datetime('Attendance Date')