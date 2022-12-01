 # I was told to resubmit this assignment, taking special consideration to naming conventions. I have adjusted all my assignments to the snake_case naming convention and optimized my variable names.

# First we need to set our secret name up for our future while loop. It needs to be a while loop because we dont know exactly how long it will take the user to figure out the answer.
secret_name = "John"

 # We also need to establish an empty list that our incorrect names can be added to.
bad_name = []

 # Now we create the while loop with a boolean
while True:
        name = input("Please enter your name: ").capitalize() # This will be our input data.
  
        if name != secret_name: # Here we have an if statement to ensure that the while loop continues if the correct answer is not given.
                bad_name.append(name) # Here we use the append function to add the incorrect answers to our empty list.
                print(name) # Here we repeat the question within the while loop.
          
        else: # If the correct answer is given, we need a condition to break from the while loop.
                break

print(f'\nFinally! Hi John! At first I thought you were {", or ".join(bad_name)}.') # Finally, we can print our final output. I also joined the badName list together to add a neat formatting display.