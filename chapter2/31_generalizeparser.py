#Generalize the above implementation of csv parser to support any delimiter and comments.
a=open("a.txt","r")
def pars(a):
	b=a.readlines()
	m=[]
	for q in b:
		if not  q.startswith("#"):
			m.append(q.split("!"))
	print m
pars(a)
