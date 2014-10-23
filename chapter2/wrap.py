a=open("she.txt","r")
def wrap(a,l):	
	b=a.readlines()
	for q in b:
		c=len(q)
		k=c/l
		m=0
		for p in range(1,k+2):
			print (q[m:p*l])
			m=p*l
	
wrap(a,30)

