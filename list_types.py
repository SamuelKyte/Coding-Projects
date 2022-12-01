# I was told to resubmit this assignment, taking special consideration to naming conventions. I have adjusted all my assignments to the snake_case naming convention and optimized my variable names. 

# This program is created to organize lists and also print two lists side by side and matching.

 # First, we need an input prompt for the first list of friend's names. I will use the .title() function here so that when this string is converted into a list, each string within the list will be capitalized.
friend_names = input("Please enter your friend's names (Separate each name with a comma (E.g. Bob, Jimmy, etc)): ").title()

 # On this line we will convert the string input by the user into a list.
friend_names = friend_names.split(", ")

 # Here is were we get the outputs from the assignment showing the indexing of our list and the len() function.
print(f"You're favorite friend is {friend_names[0]}.")
print(f"You're least favorite friend is {friend_names[-1]}.")
print(f'You have {len(friend_names)} friends.')

 # Here we have the user input the new (soon to be) list of ages.
friend_ages = input("Please enter your friend's ages in order (Separate each age with a comma (E.g. 22, 24, etc)): ")

 # This line again converst the second string of data into a list.
friend_ages = friend_ages.split(", ")

 # For the last part, I just wanted a nice format, so I researched online. This line was found at: https://stackoverflow.com/questions/48053979/print-2-lists-side-by-side
 # Basically, we join the two enumerated lists in an (x, y) format within a single variable.
result = "\n".join("{}  {}".format(x, y) for x, y in zip(friend_names, friend_ages))

 # Finally, we can take our final result and print it nicely within a formatted string.
print(f"\nYour friend's and their ages are:\n{result}")

 # I recieved feedback saying: "Also take a look at the requirements for task 1: Now, define a list called friends_ages that stores the age of each of your friends in a corresponding manner. Your code stores all three ages to the first friends name."

 # I think maybe there was a mix up, or perhaps I'm confused about which line this error is on. My code aligns two lists of names and ages and prints them side by side within a zip() function. Please correct me and provide more detail if I am mistaken.