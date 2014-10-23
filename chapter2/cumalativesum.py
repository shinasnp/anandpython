#cumalative sum of a list without using library funcion
a=[1,2,3,4]
def cumalative_sum(a):
	total=0
	s=[]
	for x in a:
		total=total+x
		s.append(total)
	print "sum" ,s

cumalative_sum(a)
