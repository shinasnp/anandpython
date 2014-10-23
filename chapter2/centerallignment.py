a=open("she.txt","r")
def center_allign(a):
	b=a.readlines()
	x=[]
	v=[]
	for q in b:
		x.append(q[ : :-1])
	print x
	for t in x:
		v.append(t)
		v.append('         ')
	print v
center_allign(a)
