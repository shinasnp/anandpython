#find unique elemnts in a list without using library function
def unique():
	#a=raw_input("enter the list")
	a=[1,2,3,1,3]
	b=[]
	for q in a:
		if q not in b:
			b.append(q)

	print b
unique()
