#cumalative product of a list without using library funcion
a=[1,2,3,4]
def cumalative_pro(a):
	pro=1
	s=[]
	for x in a:
		pro=pro*x
		s.append(pro)
	print "product" ,s

cumalative_pro(a)
