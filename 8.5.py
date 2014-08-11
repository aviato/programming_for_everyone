#~~~~~~~~~~~~~~~~~~~Coursera Assignment 8.5~~~~~~~~~~~~~~~~~~~

prompt = raw_input("please enter filename: ")
open_file = open(prompt)
count = 0

for line in open_file:
  s_line = line.split()
  if "From" in s_line:
    print s_line[1]
    count += 1
    
print "There were %d lines in the file with From as the first word" % count