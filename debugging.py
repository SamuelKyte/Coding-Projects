def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) # instead of k we need this to read key, refering to the for loop

 # homer entry needs "" not '' otherwise apostrophe will break code
 # dictionaries should be formatted with a new entry on each line
simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!",
                         "marge": "Mmm~mmmmm",
                         "homer": "d'oh",
                         "maggie": "(Pacifier Suck)" # I also go rid of a space here inside of the quotations
                        }
keys = "lisa", "bart", "homer" # outside of the function we had defined what the dictionary value would be but we didn't identify what the key values we wanted to print would be. We can simply enter whichever keys we want to get the value for and run the function.
print_values_of(simpson_catch_phrases, keys)

 # I really hope this was this simple. I was really over thinking this for a while and could not for the life of me figure it out. Sometimes simple is better?

                         
'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

