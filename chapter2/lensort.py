#sort with respect their length
a=["python","ruby","c","cplus","java"]
s=[]
j=[]
def lensort(a):
	for q in a:
		s.append(len(q))
	print s
	z=zip(s,a)
	#print z
	z.sort()
	e=len(z)
	for w in range(e):
		j.append(z[w][1])
	print j	
		
lensort(a)
		
