def descendind(a):
	freequency={}
	l=[]
	for q in a:
		freequency[q]=freequency.get(q,0)+1
	l.append(freequency)
	print l[0]
	print freequency
	k=[]
	print freequency.values().sort()
descendind('asian paintssssssss apex')
