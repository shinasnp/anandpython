def linesreverse():
	k=open("she.txt","r").readlines()
#	print k
	u=[]
	for q in k:
		u.append(q)
#	print u
	print u[: :-1]
linesreverse()
