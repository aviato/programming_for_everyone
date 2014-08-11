#~~~~~~~~~~~~~~~~~~Coursera assignment 3.1~~~~~~~~~~~~~~~~~~~~

hours = float(raw_input("Please enter your hours: "))
hourly = float(raw_input("Please enter your hourly rate: "))


pay = 0



if hours > 40:

  ot = hourly * 1.5  							# ot
  pay = 40 * hourly + (ot * (hours - 40))		# base pay + ot = pay

else:

  pay = hours * hourly 							# otherwise base pay = pay


print pay										# TGIFlol