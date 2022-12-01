# This example program is meant to demonstrate errors.

# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#The first error is that there needs to be parenthese for the print function
print("Welcome to the error program")

#should not be indented
#needs parenthese
print("\n")

#should not be indented
#ageStr's name should just be age....agestr is counter intuitive and should just be '24' so it doesn't need to be converted to an int and only one = sign
age = 24 #I'm 24 years old.

#this is all really clunky... 
#to print this well, we can write a formated line instead. We can also convert age to a str here once, so that it can still be used as an int later.
print(f"I'm {str(age)} years old.")

#Now that that looks way better, we can add other variables...
#three = 3 is unnecessary, as we can just write it into our function

answerYears = age + 3

#format this line, space after colon, answerYears variable shouldnt be in quotations, also, this line doesn't necessarily need to be printed... so ill just erase it from the code
#print(f"The total number of years: {answerYears}")

#to get answer months we need the (answerYears variable *12)+6 for an accurate depiction
answerMonths = (answerYears * 12)+6

#needs parenthese and format
print(f"In 3 years and 6 months, I'll be {answerMonths} months old.")

#HINT, 330 months is the correct answer
#it works now :)