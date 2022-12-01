 # I was told to resubmit this assignment, taking special consideration to naming conventions. I have adjusted all my assignments to the snake_case naming convention and optimized my variable names.

# The first part of this would be to create an input string. The goal of this program is to capitalize every other letter within the string.
meme=input("Please enter text: ")

 # I had to research how to do this and work backwards, as I was attempting to solve this problem based on indexing the list, which wasn't working. I found my answer here, but I rewrote the program, gave the values some new names, and added some new specifications: https://theprogrammingexpert.com/python-capitalize-every-other-letter/
 
 # Researching how to solve this problem efficiently, I found the best way would be to design a function (even though I believe we haven't covered this yet).

def meme_text(string): # We begin by designing the function. I chose to call this meme_text, as this type of string can be seen in a lot of memes. 
    result = "" # This creates an empty string for our fuction, which we can input later.
    char_cap = False # Create a boolean so the first letter is capitalized so that the function always knows where to start.
    for char in string: # This for loop is used because we only want the loop to go until the len(meme).
        if char_cap: # If and Else statements are used to differentiate between the letters that will be upper and lower case.
            result = result + char.lower()
        else:
            result = result + char.upper()
        if char != " " "!" ".": # This last if statement is extremely important as well because if the function indexed spaces or punctuation marks, the string would either not execute or not execute with the desired results.
            char_cap = not char_cap
    return result

print(meme_text(meme)) # Finally, we get our correct output.

 # I'm trying to work on my commenting; not only commenting a lot but also using PEP8 form. Please let me know if there's anything I can improve in this area!