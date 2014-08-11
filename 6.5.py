#~~~~~~~~~~~~~~~~~~Coursera assignment 6.5~~~~~~~~~~~~~~~~~~~~

str = 'X-DSPAM-Confidence: 0.8475'

find_it = str.find('0.8475')

upgrade_complete = float(str[20:])

print upgrade_complete