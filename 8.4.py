#~~~~~~~~~~~~~~~~~~~Coursera assignment 8.4~~~~~~~~~~~~~~~~~~~~

prompt = raw_input("please enter filename: ")
open_file = open(prompt)

my_list = []

for line in open_file:
  a = line.split()
  for word in a:
    if word not in my_list:
      my_list.append(word)
    else: continue


my_list.sort()

print my_list