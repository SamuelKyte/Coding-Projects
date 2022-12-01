 # I think technically this program I wrote is a little redundant because importing pyjokes already generates random jokes, but I thought I would demonstrate what I know without having to go overboard writing jokes myself.

 # First we import random and pyjokes
import random
import pyjokes

 # Just to over complicate things, I'll add an empty list.
joke_list = []

 # Now we can create a for loop for a certian number of jokes.
for i in range(0, 101):
  one_joke = pyjokes.get_joke(language="en", category="all")
  joke_list.append(one_joke) # For each random joke generated we will add it to our own joke list.

 # just to make sure that we have our own list of jokes.
print(joke_list) 

 # Now we can use the choice function to grab a random joke from our own joke list.
random_joke = random.choice(tuple(joke_list))
print(random_joke)

 # I needed help so I found information here: https://www.geeksforgeeks.org/python-script-to-create-random-jokes-using-pyjokes/
 # I also got help here: https://pynative.com/python-random-choice/#:~:text=Use%20the%20random.,this%20function%20can%20repeat%20items.