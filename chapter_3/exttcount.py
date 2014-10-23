#Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.
def extcount():
        import os
        w=os.listdir('.')
	print w
	m=0
	t=[]
	f=[]
	k=[]
	j=[]
	for q in w:
		t.append(q.split('.'))
	print t

	for i in t:	
		f.append(t[m][1])
		m=m+1
	print f
		print i[0][1]

	for r in f:
		p=f.count(r)
	print "%s:%d" %(r,p)
extcount()
