import math
#context
print("Hello! Welcome to the fully automated foundation measurement system:\n\n")

#ask user for shape of foundation
shape=input("Please enter the shape of the building's foundation that will be measured:\nYou are able to choose from: \n\nsquare \nrectangle \ntrapezoid \ncircle \nellipse \ntriangle \n\nWhat will you be measuring today:  ")

#input formula for square
if shape.lower() == 'square':
  square = input("What is the length of the foundation in feet: ")
  square = float(square)
  print(f'The area of your foundation is {round(square**2,2)} ft.')

#input formula for rectangle
elif shape.lower() == 'rectangle':
  length_r = input("What is the length of the foundation in feet: ")
  width_r = input("What is the width of the foundation in feet: ")
  length_r = float(length_r)
  width_r = float(width_r)
  print(f'The area of your foundation is {round(length_r*width_r,2)} ft.')

#input formula for trapezoid
elif shape.lower() == 'trapezoid':
  length_1_t = input("What is the first length of the foundation in feet: ")
  length_2_t = input("What is the second length of the foundation in feet: ")
  width_t = input("What is the width of the foundation in feet: ")
  length_1_t = float(length_1_t)
  length_2_t = float(length_2_t)
  width_t = float(width_t)
  print(f'The area of your foundation is {round(((length_1_t+length_2_t)/2*width_t),2)} ft.')

#input formula for circle
elif shape.lower() == 'circle':
  radius = input("What is the radius of the foundation in feet: ")
  radius = float(radius)
  print(f'The area of your foundation is {round(math.pi*(radius**2), 2)} ft.')

#input formula for ellipse
elif shape.lower() == 'ellipse':
  maj_ax = input("What is the radius of the major axis of the foundation in feet: ")
  min_ax = input("What is the radius of the minor axis of the foundation in feet: ")
  maj_ax = float(maj_ax)
  min_ax = float(min_ax)
  print(f'The area of your foundation is {round(math.pi*(maj_ax)*(min_ax), 2)} ft.')

#input formula for triangle
elif shape.lower() == 'triangle':
  length_tri= input("What is the length of the foundation in feet: ")
  width_tri = input("What is the width of the foundation in feet: ")
  length_tri = float(length_tri)
  width_tri = float(width_tri)
  print(f'The area of your foundation is {round((length_tri*width_tri*0.5), 2)} ft.')

else:
  print("\nInvalid Entry")

#This was a fun! I did a little more than I was asked but I think it was worth the time.