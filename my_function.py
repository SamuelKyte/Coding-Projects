 # Instead of just printing out the weekdays, I thought I would make a fuction that gave you a little weekly schedule.

 # Here we define our function and our parameters with missing inputs.
def weekdays():
  mon = input("What are you doing on Monday: ")
  tue = input("What are you doing on Tuesday: ")
  wed = input("What are you doing on Wednesday: ")
  thur = input("What are you doing on Thursday: ")
  fri = input("What are you doing on Friday: ")
  sat = input("What are you doing on Saturday: ")
  sun = input("What are you doing on Sunday: ")

  # Here we format the function to print it out
  print(f'''
  Your Schedule for the week is:
  
  Monday: {mon}
  
  Tuesday: {tue}
  
  Wednesday: {wed}
  
  Thursday: {thur}
  
  Friday: {fri}
  
  Saturday: {sat}
  
  Sunday: {sun}
  ''')
  return # Return the function

weekdays() # Use the function

 # Here we will do another. I got a little help just to double check things here: https://stackoverflow.com/questions/47085552/replace-every-second-word-with-the-word-hello-using-a-function

def hello(string_h):

    l = string_h.split(' ')
    
    for i in range(len(l)):
        if i % 2 == 0:    
            print(l[i], end=' ')
        else:    
            print('word', end=' ')
          
hello("Bartender can I please get a drink?")