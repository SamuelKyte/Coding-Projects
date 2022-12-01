#give the user some context

print("**You knock on the door at a party... Are you old enough to get in? ")

print(" ")

#prompt the user to enter birth year

birth_year=input("Please enter the year you were born: ")

#convert birth_year from str to int

birth_year = int(birth_year)

print(" ")

#subtract birth_year from current year to ascertain age of user

age = 2022 - birth_year

#program should check for age requirements 18+

if age >= 18:
        print("Congrats. You're in.")

#program should have a message if requirements are not fulfilled

elif age < 18:
        print("Scram baby. Come back in a few years when you're old enough.")