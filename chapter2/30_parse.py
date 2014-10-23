a=open("a.csv","r")
def parse_csv(a):
	b=a.readlines()
	v=[]
	for q in b:
		v.append(q.split(','))
	print v
parse_csv(a)
