print("Hello! Welcome to our salary calculator.")
print('')
title = input("First, are you a manager or a salesperson?\n\nFor salesperson, type 'S'. For manager, type 'M': ")

#calculate sales salary
if title.upper() == 'S':
  com = input("What were your gross sales for the month?: ")
  com = float(com)
  print(f'Your gross salary this month is R{2000.00+(com*0.08)}.')

#calculate manager salary
elif title.upper()== 'M':
  hours = input("How many hours have you worked this month?: ")
  hours = float(hours)
  print(f'Your gross salary this month is R{hours*40.00}.')