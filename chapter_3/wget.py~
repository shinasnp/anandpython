#Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.
a="http://docs.python.org/tutorial/intrept.html"
def downlode(a):
	import os.path
	import urllib
	if a[-1]=='/':
		base='index.html'
	else:
		base=os.path.basename(a)
		response=urllib.urlopen(a)
	print base,response.headers
downlode(a)
