 # I was told to resubmit this assignment, taking special consideration to naming conventions. I have adjusted all my assignments to the snake_case naming convention and optimized my variable names.

str_main=input("Please enter text: ") # First, we create an input variable.

sep_text = str_main.split(" ") # Next we use the split() function and use a space to indicate where the text should split into a list.

print('\n'.join(sep_text)) # Once our list is created out of our split string, we can join the text back together using \n to create new lines.