 # create an empty list to hold txt lines
inventory = []

 # create class
class Shoes:
     # create init function with variables
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
     # the task asked for this but it is irrelevant
    def get_cost(self):
      return self.cost
    # the task asked for this but it is irrelevant
    def get_quan(self):
      return self.quantity
     # print string of whole class
    def __str__(self):
      return f'''
      Country: \t\t{self.country}
      Code: \t\t{self.code}
      Product: \t\t{self.product}
      Cost: \t\tR {self.cost}
      Quantity: \t{self.quantity}'''

 # add txt file lines into inventory list
with open("inventory.txt", "r+") as f:
  text = f.readlines()
  for line in text[1::]:
    line = line.strip()
    line = line.split(",")
    inventory.append(line)

 # create function to see all formatted products
def view_all():
    for entry in inventory: # for loop for list
      entry = Shoes(entry[0], entry[1], entry[2], entry[3], entry[4]) # class entry
      print(Shoes.__str__(entry)) # print formatted string

 # add new products
def capture_shoe():
    shoe = [] # empty list
    country = input("Country of Origin: ") # input info
    shoe.append(country) # append list
    code = input("Code: ") # input info
    shoe.append(code) # append list
    product = input("Product Name: ") # input info
    shoe.append(product) # append list
    cost = input("Cost: ") # input info
    shoe.append(cost) # append list
    quantity = input("# in Inventory: ") # input info
    shoe.append(quantity) # append list
    
    inventory.append(shoe) # add new product to inventory list
     # rewrite inventory.txt file with updated entries
    with open("inventory.txt", "w") as f:
        f.writelines("Country,Code,Product,Cost,Quantity")
        for entry in inventory:
            entry = f'{entry[0]},{entry[1]},{entry[2]},{entry[3]},{entry[4]}'
            f.writelines("\n")
            f.writelines(entry)

 # create restock function 
def restock():
    stock = [] # empty list
    for entry in inventory:  # add quantity values to stock list as int values
        stock.append(int(entry[4])) 
    stock.sort() # sort them for from lowest to highest
    for entry in inventory:
        if str(stock[0]) == entry[4]: # find lowest stock value
            print(f'\nYour item with the lowest stock is "{entry[2]}" with only {entry[4]} in stock.') # print
    for entry in inventory:
        if str(stock[0]) == entry[4]: # find stock value
            edit = input("\nWould you like to add to stock (Y/N): ").upper() # input option
            if edit == "Y": # if yes
                amount = int(input("How man would you like to add: ")) # amount to add
                entry[4] = str(int(entry[4]) + amount) # add amount to current value, make str
                with open("inventory.txt", "w") as f: # open txt file
                    f.writelines("Country,Code,Product,Cost,Quantity") # write title of file
                    for entry in inventory: 
                        print(entry) # print all entries
                        entry = f'{entry[0]},{entry[1]},{entry[2]},{entry[3]},{entry[4]}' # create entry string
                        f.writelines("\n") # print on each line of txt file
                        f.writelines(entry) # print entry on txt file

 # create function to search for a shoe
def shoe_search():
    search = input("Enter Product Code(eg. SKU57443): ") # input code
    for entry in inventory:
        if search == entry[1]: # if code is same
            entry = Shoes(entry[0], entry[1], entry[2], entry[3], entry[4])
            print(Shoes.__str__(entry)) # print that entry

 # create function to show gross value
def gross_product_value():
    for entry in inventory: # for each item
        product = Shoes(entry[0], entry[1], entry[2], entry[3], entry[4])
        print(Shoes.__str__(product)) # print each product
        print(f'\n\t  Gross Product Value: R{int(entry[3]) * int(entry[4])}\n') # add line with formula
        print("=============================================================") # add formatting line

 # create function to show highest quantity
def high_quantity():
    stock = [] # add empty list
    for entry in inventory:
        stock.append(int(entry[4])) # add stock quantity to list
    stock.sort(reverse=True) # reverse sort
    for entry in inventory:
        if str(stock[0]) == entry[4]: # print entry with highest stock quantity
            print(f'\nYour item with the highest stock is "{entry[2]}" with {entry[4]} in stock.')
            print("\nThis item should go on sale.") # sale

 # make a menu
menu = (f'''
Please take a look at our menu options:

va - view all
ap - add product
gv - gross product value
hq - highest quantity
r  - restock
s  - search
q  - quit
''')

 # selection variable
sel = ""
while sel != "q": # while loop, quits on 'q'
    print(menu) # print menu
    sel = input("Please enter your menu selection: ").lower() # input selection
    if sel == "va": # function selection if statements
      view_all()
      pass
    if sel == "ap":
      capture_shoe()
      pass
    if sel == "gv":
      gross_product_value()
      pass
    if sel == "hq":
      high_quantity()
      pass
    if sel == "r":
      restock()
      pass
    if sel == "s":
      shoe_search()
      pass