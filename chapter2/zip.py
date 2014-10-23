#Provide an implementation for zip function using list comprehensions.
a=[2,5,7,9]
b=[7,9,2,5]
def zipp(a,b):
	i,j=0,0
	print [(a[x],b[y]) for x in range(len(a)) for y in range(len(b)) if x==y]
zipp(a,b)
