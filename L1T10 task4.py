num=input('Please enter a number: ')
num=int(num)
if num%2==0 and num%5==0:
  print(f'The number {num} is divisible by 2 and 5.')
elif num%2==0 or num%5==0:
  print(f"The number {num} is divisible by 2 or 5.\n\nLet's check for details:\n")
  if num%2==0:
    print(f'{num} is divisible by 2.')
  elif num%5==0:
    print(f'{num} is divisible by 5.')
elif num%2!=0 and num%5!=0:
  print(f'The number {num} is not divisible by 2 or 5.')
else:
  print("I don't understand.")