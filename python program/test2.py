import string
import random

def pw_gen(size = 100, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

pas=(pw_gen(int(input('How many characters in your password?'))))
# print pas
mylist=[]
test=[]
a=0
print pas
for x in pas:
	if (a==3):
		a=1
		mylist.append(test)
		# print (mylist)
		test = []
		test.append(x)
	else:
		test.append(x)
		a+=1
		# print a
print mylist		
length=len(mylist)
print length
for i in range(length):
	# print i
	for c in range(length):
		if i==c:
			pass
		elif (mylist[i]==mylist[c]):
			print "match"
		else:
			print "not match"
			
