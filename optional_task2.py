#This program will explain what to wear based on temp, weekend, and sun.
temp = input("What is the temperature outside? Reply in degrees Celsius: ")

#convert degrees from str to int
temp = int(temp)
#insert conventions for temp choice
if temp >=20:
  temp= "you should wear a short-sleeved shirt,"
elif temp <20:
  temp = "you should wear a long-sleeved shirt,"

#insert conventions for weekend choice
weekend = input("Is it the weekend? Reply 'Yes' or 'No': ")
if weekend == 'Yes':
  weekend = " shorts,"
else:
  weekend = " jeans,"

#insert conventions for sunny choice
sunny = input("Is it sunny outside? Reply 'Yes' or 'No': ")
if sunny == 'Yes':
  sunny = " and a cap."
else:
  sunny = " and a raincoat."

#final sentence
print(f'Personally, I think {temp}{weekend}{sunny}')