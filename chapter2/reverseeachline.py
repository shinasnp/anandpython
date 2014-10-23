#reverse each line in the file
def reveachline():
	f=open("she.txt","r")
	b=f.readlines()
	t=[]
	for q in b:
		t.append(q[ : : -1])
	print t
reveachline()

