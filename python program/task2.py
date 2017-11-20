import re
url_id=raw_input("enter the url with id")
id=map(int, re.findall(r'\d+', url_id))		
abc=len(id)
print abc
or_len=abc-1
print or_len
print id[or_len][2]

print id[or_len][2]

if id[or_len][6]==True:
 	print id
else:
	print "not found"



print url_id[1]
d = defaultdict(list)
for x in url_id:
   d[type(x)].append(x)

print d[int]
print d[str]
 	
for x in url_id:
	if (a==1):
		print x
	if (x=="/"):
		a=1
len_list=len(url_id)
print len_list

for x in url_id:
	if x==str:
		print "sring."
	else:
		print x