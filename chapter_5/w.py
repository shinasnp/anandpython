def w(a,result=None):
	if result is None:
		result=[]
	for x in a:
		if isinstance(x,list):
			w(x,result)
		else:
			result.append(x)
	return result
w([1,2,3,[4,5],6],)
