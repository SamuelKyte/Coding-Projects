#Prompt user for a number
e_o_test= input('Please enter a number: ')
#convert str to int
e_o_test = int(e_o_test)
#check for even or odd through use of modulus
if (e_o_test %2) ==0:
  print(str(e_o_test) + ': Even')
else:
  print(str(e_o_test) + ': Odd')