#Create while loop for count down

count_down = 20
while count_down>=0:
  print(count_down)
  count_down = count_down-1

print("=================================================================================")

#create while loop for displaying even numbers
even = 20
while even>0:
  if even%2==0:
    print(even)
  even = even-1

print("=================================================================================")
#Create while loop for *
star = "*"
while star:
  print(star)
  star = star + "*"
  if star =="******":
    break

#this final code was a bit complicated.... I found help at: https://www.pd4cs.org/example-12-find-the-greatest-common-divisor-gcd-of-two-integers/

num1 = int(input('Please input the first integer:'))
num2 = int(input('Please input the second integer:'))
while num2 != 0:
    gcd = num2
    num2 = num1 % num2
    num1 = gcd
print(f'Your greatest common divisor is {gcd}.')