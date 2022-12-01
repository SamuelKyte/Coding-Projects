#This program contains a logical error.

#The goal of this program is to get x to print itself within the range of y.

#Here I will set the values for x and the range for y
x=[47, 85, 64, 59]
y=range(1000)

#The goal is to print x for everytime is appears in y.
print(x)
for x in y:
  print(x)

#I believe this is a logical error because the program executes however, the program prints numbers 0-999, essentially printing y but not x. This requires a more difficult solution that syntax errors or runtime errors.