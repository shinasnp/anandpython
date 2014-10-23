a=['a.c','a.py','b.py','bar.txt','foo.txt','x.c']
def extsort(a):
	s=[]
	r=[]
	t=[]
	for q in a:
		s.append(q.split("."))
	#print s
	i=0
	for w in s:
		r.append(s[i][0]) 
		t.append(s[i][1])
		i=i+1
	#print r
	#print t
	z=zip(t,r)
	z.sort()
	x=[]
	o=0
	for p in z:
		x.append('.'.join([z[o][1],z[o][0]]))
		o=o+1
	print x
extsort(a)	
