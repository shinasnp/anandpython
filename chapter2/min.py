#find minimum and maximum  number in a list without using library function
a=[6,4,7,2,1]
def min(a):
	mi=a[0]
	for q in a[1:] :
		if q < mi :
			mi=q
	print mi
def max(a):
	ma=a[0]
	for q in a[1:] :
		if q > ma :
			ma=q
	print ma
min(a)
max(a)
