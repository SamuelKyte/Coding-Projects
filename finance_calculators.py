import math
#context 
print("Choose either 'investment' or 'bond' from the menu below to proceed: \n\ninvestment - to calculate the amount of interest you'll earn on your investment \nbond - to calculate the amount you'll have to pay on a home loan")

#choice
choice=input("\nPlease enter your choice: ")

#enter if statements for choice
if choice.lower() == 'investment':
  amount_i = float(input("Please enter the amount of money you are depositing (E.g. 10000): "))
  rate_i = float(input('Please enter your interest rate (E.g. 7): '))
  time_i = float(input("Please enter the number of years you plan to invest this money (E.g. 10): "))
  interest = input("Please choose 'simple' or 'compound' interest: ")
  
  #calculate simple interest
  if interest.lower() == 'simple':
    total_s = amount_i*(1+(rate_i/100)*time_i)
    print(f'\n Your total earned interest will be R{round(total_s, 2)}.')
    
  #calculate compound interest
  elif interest.lower() == 'compound':
    total_c = amount_i*(((rate_i/100)+1)**time_i)
    print(f'\n Your total earned interest will be R{round(total_c, 2)}.')

elif choice.lower() == 'bond':
  amount_b = float(input('Please enter the value of the house (E.g. 100000): '))
  rate_b = float(input('Please enter your interest rate (E.g. 7): '))
  time_b = float(input("Please enter the number of months you plan to take to repay this bond (E.g. 120): "))

  #I didn't totally understand the bond repayment formula in the text book so I am using a similar formula M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1] found on: https://www.mymove.com/mortgage/mortgage-calculation/#:~:text=For%20your%20mortgage%20calc%2C%20you,M%20%3D%20Total%20monthly%20payment
  total_b = amount_b*(((rate_b/100)/12)*(1+rate_b/100)**time_b)/((1+rate_b/100)**time_b-1)

  print(f'\n Your monthly repayment cost will be R{round(total_b, 2)}.')