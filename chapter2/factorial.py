#to find factorial without using recursion,only using product and list
def fact(x):
	f=[x]+range(1,x)
	c=1
	for q in f:
		c=c*q
	print c
fact(5)
