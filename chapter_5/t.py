import re
import os
n=[]
c=[]
def listfiles():
	a=os.listdir(".")
	return a
def readfile(l):
	for i in l:
		if not (i.startswith("#")|i.startswith("'''")):
			s=re.match(r'.\w*.py$',i)
				if s:
					print i
					print len(i)
					p=len(open(i).readlines())
					n.append(p)
	print "sum of all lines in python file is ",sum(n)
l=listfiles()
readfile(l)	

