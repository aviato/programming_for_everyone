#~~~~~~~~~~~~~~~~~~Coursera assignment 4.6~~~~~~~~~~~~~~~~~~~~

hrs = float(raw_input("hours: "))
hrly = float(raw_input("hourly: "))

def computepay(h, r):
    
  pay = h * r
  ot_pay = 40 * r + (r * 1.5 * (h - 40))
    
  if h > 40:
    return ot_pay

  else:
      return pay
  
final_pay = computepay(hrs, hrly)
print final_pay