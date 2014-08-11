#~~~~~~~~~~~~~~~~~~Coursera assignment 7.1~~~~~~~~~~~~~~~~~~~~

prompt = raw_input("please enter filename: ")
open_file = open(prompt)

for line in open_file:
  line = line.rstrip()
  print line.upper()