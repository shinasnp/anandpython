#Write a program center_align.py to center align all lines in the given file.
a=open("she.txt","r")
def center_allign(a):
        b=a.readlines()
        x=[]
        for q in b:
                x.append(q[ : :-1])
	#print x
	h=open("bis.txt","w")
        h.write("          ".join(x))
	h.close()
	h=open("bis.txt","r")
	n=h.readlines()
	h.close()
        #print n
	m=open("app.txt","w")
        for u in n:
		m.write(u[ : :-1])
	m.close()
	k=open("app.txt","r")
	result=k.read()
	print result
	k.close()


center_allign(a)           
