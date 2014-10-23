def match():
	import re
	strr='asian paints'
#	d=raw_input('asian')
	matchh=re.search('wer',strr)
	if matchh:
		print 'found',matchh.group()
	else:
		print 'not found'
match()
