#Write a regular expression to validate a phone number.
def phone():
	import re
	phone='9895123455'
	q=re.match('9895123455',phone)
	if q:
		print 'phone number matching:',q.group()
	else:
		print "not matching"
phone()

