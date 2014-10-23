#Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.
a={'x':1,'y':2,'z':3}
def invertdict(a):
	v={}
	for key,value in a.items():
		print value,key
		v[key] = value
	print v
invertdict(a)
