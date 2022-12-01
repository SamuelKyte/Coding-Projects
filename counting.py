 # I got help here: https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/

 # First we create an input variable to get our sentence.
string_one = input("Please enter a sentence: ")

 # Next we use an empty dictionary to store our occurences per letter.
occurence = {}

 # Next we need a for loop:
for i in string_one:
    if i in occurence: # Here we can add more than one occurence to the total
        occurence[i] += 1
    else:
        occurence[i] = 1
      
print(occurence)