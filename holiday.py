 # I got some help to make the code more efficient here: https://stackoverflow.com/questions/50476638/holiday-application-on-python-2-7

 # We create our first function here for hotel cost, my price being 80.59 per night.
def hotel_cost(hotel_nights):
  return hotel_nights*80.59

 # I wasn't sure how to write this ticket function so this is were I got the most help from the above citation. We basically just give three options, later seen in the input section that allows us to determine price of the ticket.
def plane_cost(destination): 
  ticket = 0
  if int(destination) == 1:
    ticket = 800
          

  elif int(destination) == 2:
    ticket = 350
          

  elif int(destination) == 3:
    ticket = 550
          

  else:
    print('\nYou have selected an invalid destination.\n\nTicket is marked as $0.')

  return ticket

 # We have our third function, easy car rental. Mine will be 150 bucks per day.
def car_rental(cr_days):
  return cr_days*150

 # Finally we can put it all together in a final function, putting all of the smaller functions inside this larger one.
def holiday_cost(hotel_nights, destination, cr_days):
  hotel_nights = hotel_cost(hotel_nights)
  destination = plane_cost(destination)
  cr_days = car_rental(cr_days)
  return hotel_nights + destination + cr_days

 # Here outside of the functions we can write the inputs for our functions so it formats nicely
hotel_nights = int(input('How many nights will you be staying? '))
destination = input('\n1. JFK\n2. LAX\n3. ATL\n\nWhere you flying to? ')
cr_days = int(input('\nHow many days will you need a car for?: '))
total = holiday_cost(hotel_nights, destination, cr_days)
print(f'\nYour total cost for your holiday is ${total}.')