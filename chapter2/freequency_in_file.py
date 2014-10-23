a=open("she.txt","r")
def freequency(a):
	b=a.read().split()
	print b
	for w in b:
		word_freequency(w)
	'''for word,count in freequency.items():
		print word,count'''
def word_freequency(t):
	freequency={}
	for q in t:
		freequency[q]=freequency.get(q,0)+1
	print freequency
	for word,count in freequency.items():
                print word,count

freequency(a)
