a=[5,6,9,8,7,2,5,4,3,9]
def group(a,s):
	b=len(a)
	c=b/s
	print c
	m=0
	list=[[] for t in range(c+1)]
	print list
	for q in range(c+1):
		for w in a[m:s*(q+1)]:
			list[q].append(w)
		m=s*(q+1)
		print m
	#print list
	if list[-1]==[]:
		del list[-1]
	print list
group(a,3)
