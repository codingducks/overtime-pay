while True:
 try:
  hours = float (raw_input('How many total hours did you work?\n'))
  overtime = float(raw_input('How many of those hours were overtime?\n'))
  wage = float(raw_input('What is your regular rate?\n'))
  otwage = float(raw_input('What is your overtime rate?\n'))
 except:# code will already try to convert string to float, will crash if it cannot
  print('Please start over, enter numbers in all fields, use 0 if not applicable\n') 
  continue #restarts loop 
 if overtime > hours:
  print 'Overtime cannot be greater than total hours worked, Please start over\n'
 else: #corect input entered
  break # out of the loop


#if no over time worked spits out pay
if overtime == 0:
 pay = hours * wage
 print pay
#if overtime worked spits out pay
elif overtime > 0:
 pay = (hours - overtime) * wage + overtime * otwage
 print pay 

