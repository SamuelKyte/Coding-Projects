#If I understand this assignment correctly, the timestables only go to 12:

#prompt user to enter a number
num=int(input("Please enter a number: "))
#create a list to hold multiplication table sequence
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#create for loop
for x in range(1,13):
  print(str(num) + "*" + str(x) + "=" + str(num*x))