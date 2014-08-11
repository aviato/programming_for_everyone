#~~~~~~~~~~~~~~~~~~Coursera assignment 3.3~~~~~~~~~~~~~~~~~~~~

score = raw_input("Please enter your score (a number between 1.0 and 0.0): ")
grade = float(score)

if grade >= 0.9:
  print "A"

elif grade >= 0.8:
  print "B"

elif grade >= 0.7:
  print "C"

elif grade >= 0.6:
  print "D"

elif grade < 0.6:
  print "F"

else:
  print "Invalid entry. Please try again."
  
