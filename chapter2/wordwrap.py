a=open("she.txt","r")
def wordwrap(a,l):
	b=a.readlines()
	for q in b:
		m=0
		for j in b:
			while(j[m+l]<>' '):
				(m+l)=(m+l)-1
			print q[m:m+l]
			m=m+l	
							
wordwrap(a,3)             
