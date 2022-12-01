#first get height and weight data
height = input("Please enter your height in meters: ")
weight = input("\nPlease enter your weight in kilograms: ")

#convert str to float
height = float(height)
weight = float(weight)

#create BMI calculator
bmi = weight/(height*height)
print(f'Your BMI is: {round(bmi,2)}.\n')

#create metrics for user
if bmi >=30:
  user = 'obese'
elif bmi >=25 !=30:
  user = 'overweight'
elif bmi >=18.5 !=25:
  user = 'normal'
elif bmi <18.5:
  user = 'underweight'

print(f'According to your BMI, you are {user}.')