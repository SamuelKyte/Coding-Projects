 # Create a boolean for the num variable in the while loop.
num = True

 # Create the while loop and an input variable.
while num:
      num=int(input('Please enter a number less than or equal to 100: '))
      if num >100: # Create a condition for the while loop to prompt user to follow instructions.
          print("\nPlease follow instructions!")
          continue

      elif num<=100: # Set conditions for if instructions are followed.
            if num%2==0:
                  print(f'{num} is even and {num} multipied by 2 is {num*2}.')
                  break
            elif num%2==1:
                  print(f'{num} is odd and {num} multipied by 3 is {num*3}.')
                  break