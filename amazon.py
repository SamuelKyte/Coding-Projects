''' I looked at https://stackoverflow.com/questions/57902594/python-reading-lines-in-a-txt-file-and-writing-to-new-txt-file for some help although the code there was in my opinion a little gnarly and outdated...

Line 14: We want to do some formatting to what we are reading before we can calculate and export it. We want this to be within a for loop in order to do this with each line and only for our lines.

Line 21: Here we set our conditions. If the text demands a specific calculation, the numbers will be calculated accordingly, converted into strings, and printed within a formatted string.
'''

import math # We can import math for our function

def help(): # Here we create our function, I called it help because this was tricky for me today.
      with open("input.txt", "r") as f: # We can open our first input text file and read it
            text = f.readlines() # Thanks to Darren Noortman for the tip here!
        
            with open("output.txt", "w") as fp: # Then we open a new txt file to write our export
                
                for line in text:
                    op, nums = line.split(':') # The colon allows us to seperate the desired calculation from the numbers
                    op = op.strip("")
                    nums = list(map( float, nums.strip().split(',') )) # Here we can convert from strings to floats in order to do the calculations.

                    if op == 'avg' :
                        avg = sum(nums)/len(nums)
                        fp.write(f'The {op} of {nums} is {str(avg)}.\n')
                    elif op == 'min' :
                        minimum = min(nums)
                        fp.write(f'The {op} of {nums} is {str(minimum)}.\n')
                    elif op == 'max' :
                        maximum = max(nums)
                        fp.write(f'The {op} of {nums} is {str(maximum)}.\n')
                    else :
                        print('wrong operation')
            
            fp.close() # And we close our files up nicely
help() # run function
