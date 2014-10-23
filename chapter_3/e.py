import os
def directory(path):
  list_dir = []
  list_dir = os.listdir(path)
  count = 0
  for file in list_dir:
	#if file.endswith(".py"): # eg: '.txt'
      		count += 1
  print count
directory(".")

