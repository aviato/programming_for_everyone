#~~~~~~~~~~~~~~~~~~Coursera assignment 5.2~~~~~~~~~~~~~~~~~~~~

largest = None
smallest = None

while True:
  prompt = raw_input("Please enter a number: ")
  
  try:
    num = float(prompt)
    
    if smallest == None or num < smallest:
      smallest = num
      
    elif largest == None or num > largest:
      largest = num
      
      
  except:
    if prompt == 'done':
      break
      
    else:
      print "Invalid input (not a number)."
      
print "Maximum", largest
print "Minimum", smallest