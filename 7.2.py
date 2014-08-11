#~~~~~~~~~~~~~~~~~~~Coursera assignment 7.2~~~~~~~~~~~~~~~~~~~

prompt = raw_input("please enter filename: ")
open_file = open(prompt)

num_list = []
count = 0
total = 0
keyword = "X-DSPAM-Confidence:"

for line in open_file:
  if keyword in line:
    line = line.split()
    num = float(line[1])
    num_list.append(num)
    count += 1

for num in num_list:
  total += num
  
print "Average spam confidence:", total / count

# ~~~~~~~~~~~~~~~~~~~~Alternate solution~~~~~~~~~~~~~~~~~~~~~

# n/a