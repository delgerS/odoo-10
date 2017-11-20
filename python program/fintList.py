

mylist=['1:admin', '500:NOONI', '512:pOONI', '513:FAROOQ', '514:HABIB', '515:ASGHAR', '516:MAHTAB', '517:HASEEB', '5117:USMAN', '600:HAIDER', '700:REHMAN', '2\x000:yasir', '3\x000:Kamran', '10:faisal', '9:har', '8:irfan', '6:ali', '11:frd', '12:new', '13:api user', '14:test user', '15:new user', '17:yasir16', '16:yasir15', '7:yasir1', '18:kamran123', '22:rehaman bahi', '23:fksdhfdsfdsfd', '24:dasdsaddsad', '25:dasdasdasdd', '26:fdfdfsgsgsfgs', '27:sasasasa', '28:rauf444', '29:rauf222', '30:awais ecube', '31:awais31', '32:awais32', '34:awias34', '36:awasi36', '37:nayab ecube', '41:kamran41', '42:kamran42', '43:kamran43', '44:kamran44', '45:yasir45', '46:yasir466', '47:yasir47', '48:yasir48', '49:yasir49', '50:yasir50', '51:yasir51', '52:ather']
# print mylist[1]

for x in mylist:
	abc=x.split(":")
	if abc[0]=='513':
		abccc = abc[1]
		print abccc
		break
		
