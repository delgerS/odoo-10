import os
os.chdir('/home/odoo/Desktop/odoo10git')
os.system('git init')
os.system('git remote add origin https://github.com/khyasir/odoo-10.git')
os.system('git add *')
os.system('git status')
os.system('git commit -m "this is your comment"')
master='git push origin master'
os.system('echo %s' % (master))
username='khyasir'
password='yasir43'
# os.system('echo %s' % (username))
# os.system('echo %s' % (password))