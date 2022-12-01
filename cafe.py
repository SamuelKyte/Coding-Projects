 # First I made a list of my menu items.
menu = ["coffee", "tea", "muffin", "bagel"]

 # For my first dictionary, I demonstrate the amount of each item. The keys hold the name of each item, the values hold the stock amount.
stock = {'coffee': 15,
         'tea': 15,
         'muffin': 10,
         'bagel': 10
        }

 # For my second dictionary, I demonstrate the price of each item. The keys hold the name of each item, the values hold the price.
price = {'coffee': 5.00,
         'tea': 2.50,
         'muffin': 3.50,
         'bagel': 4.50
        }

 # For my third dictionary I will demonstrate total value in store for each individual item. The keys hold the name of each item, the values are stock amount multiplied by price. I got help here: https://bobbyhadz.com/blog/python-multiply-two-dictionaries
total_i = {key: stock[key]*price[key] for key in stock}

 # Finally I can create and print my final value of total store inventory price by adding all of the values together in the total_i dictionary.
total_w = sum(total_i.values())
print(total_w)