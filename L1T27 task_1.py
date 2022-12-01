'''For this calculator, I design a function with three parameters: 2 floats and an operator. I have entered defensive programming but if there are mistakes, please let me know. 

To test if the num1 or num2 are strs I used try/except method from: https://stackoverflow.com/questions/16488278/how-to-check-if-a-variable-is-an-integer-or-a-string
'''

def calc(num1, num2, oper):
      # I chose floats instead of ints because capability is maxed
      try: 
          num1 = float(num1) 
      except: 
          print("Your first choice was not a number...")
          exit() # if input is not number, exit program
      try: 
          num2 = float(num2)
      except: 
          print("Your second choice was not a number...") 
          exit()
      if num2 == 0 and oper == '/': # defensive prog for division by 0
          print("Numbers cannot be divided by 0.")
          return
      # Allow a certian number of operators
      if oper == '+':
          return num1 + num2
      elif oper == '-':
          return num1 - num2
      elif oper == '*':
          return num1 * num2
      elif oper == '/':
          return num1 / num2
      else: # if invalid operator is selected, exit program
          print("Invalid Operator"); exit()


 # I used a while loop to continue the program until closed.
 # design 3 options for loop
loop = True # boolean for while loop
while loop == True:
      message = input("Enter a calculation(CALC), view calc history(VIEW), or close the application(CLOSE): ").upper() # create menu options
      if message == "CALC": # set calculator
          num1=input("\nPlease enter a number: ") # create inputs for function arguments
          num2=input("\nPlease enter a number: ")
          oper=input("\nPlease enter a operator (eg. +, -, *, /): ")
          result = calc(num1, num2, oper) # create variable for result
          line = (f'{num1} {oper} {num2} = {result}') # formatted string for ease of .txt writing
          print(line)
          print("\n") # make sure each calc is written on seperate lines
          with open("answers.txt", "a") as f: # write calc
            f.write(str(line)+"\n")
            f.close()
      elif message == "VIEW": # view all calcs inside .txt
          with open("answers.txt", "r") as f:
            for line in f:
                print(line.rstrip())
      elif message == "CLOSE": # keep loop until user closes
          exit()
      else: # create defense for invalid selection
          print("\nUnknown Command\n")
          pass

'''Please let me know if any corrections can be made. Thank you!'''