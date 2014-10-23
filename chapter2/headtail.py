#Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
a=open("she.txt","r")
m=open("she.txt","r")
def head(a):
	w=[]
	b=a.readlines()
	for q in range(10):
		w.append(b[q])
	print w
	a.close()
def tail(m):
	t=[]
	b=m.readlines()
	print b
	c=len(b)
	print c
	k=c-10
	print k
	for s in range(k,c):
		t.append(b[s])
	print t
	m.close()
head(a)
tail(m)

