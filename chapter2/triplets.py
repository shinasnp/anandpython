#Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet.


def triplets(a):
	print [(p,q,r) for p in range(1,a) for q in range(p,a) for r in range(q,a) if p+q==r]
triplets(5)

