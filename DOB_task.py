 # First I want to import and open the file. I already have the DOB.txt in another tab alongside my python main file, so I can just use the open function.

 # I also use the ( , 'r+') in order to read and edit the file.
f = open('DOB.txt', 'r+')

 # I thought it would be nice to print out the txt file name just so we know for sure which file we are redng/editing.
print(f.name)

 # Get nice spacing for a good format.
print("\n")

 # Set up a for loop to creat a pattern for each line of the file to follow.
for line in f:
        line = line.split(" ") # I split each line into a list so that I could edit the format better.
        print("Name\n") # I created a space for name to display.
        print(" ".join(line[0:2])+"\n") # Here I only wanted to display and join the indexed positions of names.
        print("\nBirthdate\n") # I created a space for the Birthdate to be displayed.
        print(" ".join(line[2:])+"\n\n") # # Here I only wanted to display and join the indexed positions of birthdates.

print("\n") # Again, nice spacing.

f.close() # Finally, I close the file when I'm done using it.