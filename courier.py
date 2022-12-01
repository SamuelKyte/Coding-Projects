#create context
print("Hello! Welcome to our courier delivery system.\n")

#prompt user for package price
pack_price = input("Please enter the price of the package you are purchasing with us: ")

#convert pack_price from str to float
pack_price = float(pack_price)

dist = input("Please enter the distance the package will be travelling in kms: ")

dist = float(dist)

print(' ')
print("Thank you! \n\nI just have a few more questions before we can continue.\n")

#create variable for total cost
total_cost = pack_price

#prompt categories
ship = input("How will your package be delivered? \nReply with 'AIR' or 'FREIGHT': ").upper()

#calculate option choice
if ship == 'AIR':
  total_cost = total_cost + (dist*0.36)
elif ship == 'FREIGHT':
  total_cost = total_cost + (dist*0.25)
else:
  print('invalid entry')

insur = input("Would you like to be full insurance for R50.00, limited insurance for R25.00, or no insurance? \nReply with 'FULL', 'LIMIT', or 'NONE': ").upper()

#calculate option choice
if insur == 'FULL':
  total_cost = total_cost + 50
elif insur == 'LIMIT':
  total_cost = total_cost + 25
elif insur == 'NONE':
  total_cost = total_cost + 0
else:
  print('invalid entry')

gift = input("Would you like us to gift wrap this package for R15.00?\nReply 'YES' or 'NO': ").upper()

#calculate option choice

if gift == 'YES':
  total_cost = total_cost + 15
elif gift == 'NO':
  total_cost = total_cost + 0
else:
  print('invalid entry')

speed = input("Would you like to upgade your package to priority mail for R80.00?\nReply 'YES' or 'NO': ").upper()

#calculate option choice
if speed == 'YES':
  total_cost = total_cost + 100
if speed == 'NO':
  total_cost = total_cost + 20

#print total cost and round to hundreth decimal place for currency
print(f"Thank you for your patronage.\nYour total for this package is: R{round(total_cost, 2)}.")