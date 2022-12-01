 # First I'll create a variable to ask how many students will register:
num_stu = input("How many students are registering: ")

 # Then for the for loop we need that variable to be an int so that we can use its length for the for loop:
num_stu = int(num_stu)

 # Now we need an empty list so that the for loop can give us all of the student id numbers in one place.
id_list = []

#now we create that for loop:
for i in range(num_stu):
        id_num = input("Please enter your/their student ID number: ") # This question should be posed for the amount of students registering.
        id_list.append(id_num) # Every entry will be sent to our empty list that we established above.

 # I discovered through trial and error that a list cannot be written to a .txt file so we have to join our list using new line spacing before we can export the data.
id_list = "\n".join(id_list)

 # Finally we can open up our newly written .txt file, upload our data and close it up. I added a line of text as well just so that later when we read the exported data it looks a little clearer.
with open('reg_form.txt', 'w') as f:
  f.write("Student ID Numbers:\n")
  f.write(id_list)
  f.close()