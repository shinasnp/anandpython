n='ells'
def grep(n):
	a=open("she.txt","r")
	b=a.readlines()
	print b
	for q in b:
		if n in q:
			print q
grep(n)

