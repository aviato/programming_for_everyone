#~~~~~~~~~~~~~~~~~~~Coursera assignment 9.4~~~~~~~~~~~~~~~~~~~

prompt = raw_input("please enter filename: ")
open_file = open(prompt)

my_dict = {}

big_sender = None
count = 0

for line in open_file:
  if "From: " in line:
    split_line = line.split()
    email = split_line[1]
    if email not in my_dict:
      my_dict[email] = 1
    else:
      my_dict[email] = my_dict[email] + 1
      
for key, value in my_dict.items():
  if value > count:
  
    big_sender = key
    count = value

print big_sender, count
    


    