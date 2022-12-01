 # I was told to resubmit this assignment, taking special consideration to naming conventions. I have adjusted all my assignments to the snake_case naming convention and optimized my variable names.

 # First we need a prompt to input text. I also put in the .lower() function so that there are no errors when it comes to capitalization in the inputs. Plus, it looks nicer in the final output.
text = input("Please enter a sentence: ").lower()

 # Now we need a variable and prompt to erase specific characters. Again, I used the .lower() to ensure proper matching with the first input.
disappear = input("Please enter what characters you would like to erase(seperate each character with a comma and space(E.g. a, e, i, o, u)): ").lower()

 # Now we need to take the disappear string and seperate each variable we want to be erased.
dis_sep = disappear.split(", ")

 # I wanted to print our disSep list just to give the user and myself some confirmation that everything looks right.
print(f' The variables that will be erased are {dis_sep}.')

 # Here I used a for loop because the string formatting methods don't work for lists, only strings. Basically, I could either work to replace each character individually, or I could use i to index each variable in my list and a for loop to erase each one.
for i in dis_sep:
      text = text.replace(i, "") # Also, i used replace because through trial and error, the strip method still didn't work within my for loop. 
print(text.capitalize()) # I capitalized this final print out just so that the formatting looks nice on the final product sentence. 

 # Screaming because I actually figured this out through experimentation on my own when I couldn't find the answers I wanted through research! Also, I'm finally using the PEP8 method of 4 indentations within my conditions, so I hope it looks a little cleaner. Please let me know if format wise anything could be improved.