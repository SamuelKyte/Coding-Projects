# This example program is meant to demonstrate errors.

# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#str animal needs quotes and should be lowercase based future use
animal = "lion"
animal_type = "cub"
number_of_teeth = 16

#wrong structure for formated sentence, variables in the wrong places
full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth.")

#needs parenteses
print(full_spec)