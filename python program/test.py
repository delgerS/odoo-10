import re
url_id=raw_input("enter the url with id")
id=map(int, re.findall(r'\d+', url_id))      
print id[0]
if int in my id:
   print "integer"
else:
   print "string"
   


