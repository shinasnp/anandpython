def filter(even,a):
	print even(a) 
def even(a):
	print [x for x in a if x%2==0]
	
filter(even,range(10))
