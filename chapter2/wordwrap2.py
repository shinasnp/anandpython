a=open("she.txt","r")
def wrap(a,l):
        b=a.readlines()
        for q in b:
                c=len(q)
                k=c/l
                m=0 
                for p in range(1,k+2):
			if (q[p*l]==' '):
                        	print (q[m:p*l])
                        	m=p*l
			break
		#	else:
		#		print (q[m:(p*l)-1])
		#		m=(p*l)-1

wrap(a,5)


