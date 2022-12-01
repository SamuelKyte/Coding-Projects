#provide the user context
print('''Hello! Welcome to our system.

We just need to ask you a few questions before we begin.''')
print(" ")
#prompt user to input name
full_name = input("Please enter your full name: ")

#This format was quite complicated but I started to think of it as a password. You must have " ", it must be a certain amount of characters, etc. I found some additional information here: https://www.geeksforgeeks.org/python-program-check-validity-password/

#value for space is zero so that python can search and fulfill requirement of 2+ names
space = 0

#checking for max and min char limit
if len(full_name) > 4 and len(full_name)<= 25:
    for i in full_name:
        #checking for space or 2+ names entered.
        if i == " ":
            space+=1             
if space==1:
  print("Thank you for entering your full name!")
elif len(full_name) ==0:
  print("You haven’t entered anything. Please enter your full name.")
elif len(full_name)<=4:
  print( "You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif len(full_name)>25:
  print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else:
    print("Are you sure that's your full name? \nPlease try again...")
#**I think this fulfills the requirements, but I'm wondering how this could become a loop to feed back into the initial question until the requirements have been satisfied.**