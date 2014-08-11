prompt = raw_input("Please enter filename: ")
open_file = open(prompt)

times = dict()
data = list()
most_pop = 0

for line in open_file:
  if "From " in line:
    s_line = line.split()
    element = s_line[5]
    sl_ele = element[:2]
    times[sl_ele] = times.get(sl_ele, 0) + 1

for key,value in times.items():
  data.append( (key, value) )
  
data.sort()

for key, value in data:
  print key, value
    
