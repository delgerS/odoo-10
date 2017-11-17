# -*- coding: utf-8 -*-
from zklib import zklib
from zklib import zkconst
from datetime import datetime , timedelta
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pyvirtualdisplay import Display
import xmlrpclib

from openerp import models, fields, api
from openerp.exceptions import Warning
from odoo.exceptions import UserError
from openerp.exceptions import UserError
import config


class hr_create_user_bio_machine(models.Model):
	_inherit = 'hr.employee'
	@api.model
	def create(self, values):
		zk = zklib.ZKLib(config.key['ip'], int(config.key['port']))
		res = zk.connect()
		if res == False:
			zk.enableDevice()
			zk.disableDevice()
			print zk.getUser()
			zk.enableDevice()
			zk.disconnect()
		result = super(hr_create_user_bio_machine, self).create(values)
		return result


	@api.multi
	def createBioUsers(self):
		zk = zklib.ZKLib(config.key['ip'], int(config.key['port']))
		res = zk.connect()
		if res == False:
			zk.enableDevice()
			zk.disableDevice()
			BioUsers = zk.getUser()
			for user in BioUsers:
				if (BioUsers[user][0] == str(self.id)):
					raise Warning('User Already Present in Machine.')
			zk.setUser(uid=False, userid=str(self.id), name=str(self.name), password='', role=zkconst.LEVEL_USER)

			zk.enableDevice()
		zk.disconnect()
		display = Display(visible=0, size=(800, 600))
		display.start()
		browser = webdriver.Firefox(executable_path=r'/home/rocky/Downloads/geckodriver')
		browser.wait = WebDriverWait(browser, 5)
		browser.get('http://192.168.100.29')
		xpaths = { 'username' :   "//input[@name='username']",
				   'passwd' : "//input[@name='userpwd']",
				   'login' : "//input[contains(@value,'Login')]",
				 }

		print "Browser is opened"

		browser.find_element_by_xpath(xpaths['username']).clear()
		browser.find_element_by_xpath(xpaths['username']).send_keys('1')
		print "username is typed"
		browser.find_element_by_xpath(xpaths['passwd']).clear()
		browser.find_element_by_xpath(xpaths['passwd']).send_keys('1234')
		print "password is typed"
		browser.find_element_by_xpath(xpaths['login']).click()
		browser.get('http://192.168.100.29/form/Device')
		time.sleep(50)
		browser.quit()
		print "browser Closed"
		display.stop()

	@api.model
	def _updateAttendance(self):
		zk = zklib.ZKLib(config.key['ip'], int(config.key['port']))
		common =  xmlrpclib.ServerProxy('%s/xmlrpc/2/common' % config.key['odooserver'])
		common.version()
		uid = common.authenticate(config.key['db'], config.key['odooLogin'], config.key['odooPasswd'], {})
		api = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' % config.key['odooserver'])
		try:
			res = zk.connect()
			zk.enableDevice()
			zk.disableDevice()
			info = []
			attendance = zk.getAttendance()
			actualServerTime = str(datetime.now())
			requiredServerTime = actualServerTime.split('.')
			requiredServerDate = requiredServerTime[0].split(' ')
			if (attendance):
				for lattendance in attendance:
					time_att = str(lattendance[2].date()) + ' ' +str(lattendance[2].time())
					atten_time1 = datetime.strptime(str(time_att), '%Y-%m-%d %H:%M:%S')
					atten_time = atten_time1 - timedelta(hours=5)
					atten_time = datetime.strftime(atten_time,'%Y-%m-%d %H:%M:%S')
					attenDate = str(atten_time).split(' ')
					if (requiredServerDate[0] == attenDate[0]):
						data = {
						'user_id' :lattendance[0],
						'Date' : str(lattendance[2].date()),
						'Time' : str(lattendance[2].time()),
						'DateTime' : atten_time
							}

						info.append(data)
				allOdooAttendance = api.execute_kw(config.key['db'], uid, config.key['odooPasswd'],
				 'ecube.raw.attendance','search_read',[],
				 {'fields': ['employee_id', 'attendance_date', 'name']})
				for rec in info:
					if (rec['DateTime'] not in [odooAtten['attendance_date'] for odooAtten in allOdooAttendance]) and rec['user_id'] not in [odooAtten['employee_id'][0] for odooAtten in allOdooAttendance]:
						api.execute_kw(config.key['db'], uid, config.key['odooPasswd'], 'ecube.raw.attendance',
						'create', [{
									'employee_id': rec['user_id'],
									'attendance_date': rec['DateTime'],
									'name': config.key['ip'],
									}])
		except Exception, e:
			print "Process terminate : {}".format(e)
		finally:
			if zk:
				zk.disconnect()

# Steps that required for this F*****G machine
# Install https://github.com/dnaextrim/python_zklib this library
# Install Selenium
# Download Gekodriver
# Export path of Geckodriver
# Install sudo apt-get install xvfb
#install sudo pip install pyvirtualdisplay