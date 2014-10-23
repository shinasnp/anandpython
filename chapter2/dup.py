#find duplicate elements in a list
def dups():
	a=[5,9,7,5,7,3,6,6]
	b=[]
	j=[]
	for q in a:
		if a.count(q)>1:
			 b.append(q)
	print b
	for w in b:
		if w not in j:
			j.append(w)
	print j
	
dups()
