# student_name=["yasir","kamran","aqeel"]
# student_name[1]="mustafa"
# print student_name[1]
# student_name.append("basit")
# print student_name[3]
# print student_name
# if student_name[0] == "yasir":

# 	print True
# else:
# 	print False
# #   #why
# # print len(student_name)
# del student_name[1]
# for x in xrange(1,10,3):
# # 	x+=1+2
# # 	print "number is {0}".format(x)
# # for name in student_name:
# # 	if name=="kamran":
# # 		continue
# # 		print "name found "+name
		
# # # 	print "curently testing "+name
# # x=0
# # while x<=10:
# # 	print x
# # 	x=x+2
# #  
# student_name={
# "name":"yasir",
# "student_id":12345,
# "feeback":None,
# }
# # print student_name["feeback"]
# # print student_name.keys()
# # print student_name.values()
# # print student_name["name"]
# student_name["name"]="bilal"
# student_name["last_name"]="rauf"
# print student_name["student_id"]
# del student_name["feeback"]
# try:
# 	id_card=student_name["last_name"]
# 	abc=2+id_card
# 	print "id_card found"
# except KeyError:
# 	print "id_card not fount in dictionaries"
# except TypeError as Error:
# 	print "same type of no add"
# 	print (Error)

# All_student=[{
# 	"name":"bilal", "student_id":12344},
# 	{"name":"khan" , "student_id":1122
# }]
# print All_student[0]["name"]
# print All_student[1]["student_id"]

#tuples
# tup1 = ('physics', 'chemistry', 1997, 2000);
# print tup1[3]


# a=1
# b=17
# for x in xrange(10,0,-1):
# 	print x*" " + a*"*"
# 	a+=2
# for s in xrange(2,11,+1):
# 	print s*" "+b*"*"
# 	b-=2	
# def function_name(a,b):
# 	"this is my 1st function"
# 	c=a+20
# 	print c
# 	return c
# function_name(20,30)

# def changeme():
#    print "This changes a passed list into this function"
#    mylist[1]=22
#    print "Values inside the function: ",mylist
#    return
# mylist=[10,20,30]
# changeme()   

# def test(age,name="aqeel"):
# 	"this info name and age"
# 	print "agess",age
# 	print "nameddd",name
# test(age=20)	

def printinfo( arg1, *abc ):
   print "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in abc:
      print var
   return;
printinfo(10,20,30,"abc","2bc")   