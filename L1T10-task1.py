#assign three variables random values
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
num3 = input("Enter a number: ")

#convert variables from strings to integers
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

#compare the numeric values of variables
if num1 > num2:
  print(f'{num1} is greater than {num2}.')
else: 
  print(f'{num2} is greater than {num1}.')

#determine if values are odd or even
if num1%2 ==1:
  print(f'{num1} is odd.')
else:
  print(f'{num1} is even.')
 
if num2%2 ==1:
  print(f'{num2} is odd.')
else:
  print(f'{num2} is even.')

if num3%2 ==1:
  print(f'{num3} is odd.')
else:
  print(f'{num3} is even.')

#conditional statement to sort values of variables from greatest to least
print("\nHere are your values from greatest to least: \n")
if num1 >= num2 >= num3:
  print(num1, num2, num3)
elif num2 >= num1 >= num3:
  print(num2, num1, num3)
elif num2 >= num3 >= num1:
  print(num2, num3, num1)
elif num1 >= num3 >= num2:
  print(num1, num3, num2)
elif num3 >= num1 >= num2:
  print(num3, num1, num2)
elif num3 >= num2 >= num1:
  print(num3, num2, num1)

#**I am wondering if there is a more efficient way to do this using conditionals... I'm aware that there are more efficient ways to do this WITHOUT using conditionals though...
#Thanks! :)