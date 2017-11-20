# x = 'blue,red,green'
# x.split(",")
# a,b,c = x.split(',')
# print a,b,c
myList=["ddd",2323]
from collections import defaultdict
d = defaultdict(list)
for x in myList:
   d[type(x)].append(x)

print d[int]
print d[str]