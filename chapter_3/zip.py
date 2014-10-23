import zipfile
def zip():
	z=['c.zip']
	for q in z:
		j=zipfile.is_zipfile(q)
		print j
zip()
