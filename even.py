 # First create a variable for the user's input.
user=input('Please enter an even number: ')

 # Define i value
i=0

 # Create a while loop. Here I set the value for i extremely high because I didn't know the rule for infinity but basically I wanted this program to work for almost any number.
while i<=1000000000000000:
      if i%2==0: # Here we create an if statement to check if i is even by using the modulus
            print(i) # The print i and i+=2 within the while loop work together to display all even numbers up to the users number entered.
            i+=2
      if i==int(user)+2: # Here we create a break condition for the while loop to display their number but nothing higher.
            break
      elif int(user)%2!=0: # Here is our elif condition setting conditions for if our number is odd.
            print('Your response is odd.')
            break

#The only part I don't understand here is why when an odd number is entered, it still prints i as 0. How would I get rid of that?