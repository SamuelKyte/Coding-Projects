'''This is just getting easier and easier!'''

 # create an adult class
class Adult:
   # initialize it with values
  def __init__(self, name, age, hair, eye):
    self.name = name
    self.age = age
    self.hair = hair
    self.eye = eye
   # insert drive fuction
  def can_drive(self):
      return "Can drive"

 # create subclass of Adult
class Child(Adult):
  #override drive function
  def can_drive(self):
      return "CANNOT DRIVE"

  
'''For the next part I am creating input variables and choices to pick which class will better suit the user based on age. For the Adult class initialization, remember that we need to fulfill all variable needs: name, age, hair_col, eye_col.'''

 # input name
name = input("Please enter your full name: ")

 # create a try/except loop to verify an int value for age
while True:
    try:
        age = int(input("Please enter your age: "))
        break
    except:
        print("That's not a valid option!")

 # input hair color
hair_col = input("Please enter your hair color: ")

 # input eye color
eye_col = input("Please enter your eye color: ")

 # if & elif statements to sort class suitability based on age
 # formatted print when sorted
if int(age) >= 18:
  user = Adult(name, age, hair_col, eye_col)
  print(f''' 
  {user.name}
  {user.age}
  {user.hair}
  {user.eye}
  {Adult.can_drive(user)}
  ''')

if int(age) < 18:
  user = Child(name, age, hair_col, eye_col)
  print(f''' 
  {user.name}
  {user.age}
  {user.hair}
  {user.eye}
  {Child.can_drive(user)}
  ''')

 # And that should be it!