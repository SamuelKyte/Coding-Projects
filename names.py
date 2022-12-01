 # Create a list to hold name variables.
name_list = []

 # Before, I had the name = input("Please enter a student's name: ") above the while loop, but it would reject the first name entered. This is why I thought I could add a boolean being true to hold the name variable before the while loop and adapting it later.
name = True

 # Create the while loop because the amount of names that will be input by the user is unknown.
while name:
      name = input("Please enter a student's name: ") # Create an input variable.
      name = name.capitalize() # Format the names to look nice, but also ensure that "Stop" is always excepted.
      name_list.append(name) # Add a new name to name_list.
  
      if name=='Stop': # Create a condition for a break in the loop.
            name_list.remove("Stop") # Remove the appended 'stop' variable.
            print(name_list) # Print the list.
            print(f'There are {len(name_list)} students present.') # Print length of list
            break