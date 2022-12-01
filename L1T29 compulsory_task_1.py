"""
Compulsory Task 1: 
------------------

Use the code provided copied to a new file named compulsory_task_1.py: 
1. Add another method in the Course class that prints the head office location: Woodstock, Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id

These methods should all print out the correct information to the terminal

On a side note, this task covers single inheritance. multiple inheritance is also possible in Python and we encourage you to do some research on multiple inheritance when you have finished this course.
"""

'''
This was a challenging project to start but once you get the hang of it, it was incredibly easy! I got help here: https://www.youtube.com/watch?v=RSl87lqOXDE.
'''

 # make your Course class
class Course:
     # add class variables
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    location = "Woodstock, Cape Town"

     # because I want to add students to this (like enrollment letters)
     # each student class will initialize with name and inherit other values
    def __init__(self, first, last):
        self.first=first
        self.last=last

     # create function to print full name
    def fullname(self):
        return "{} {}".format(self.first, self.last)

     # function to print website info
    def contact_details(self):
        return f"Please contact us by visiting: {self.contact_website}."

     # function to print head office location
    def location_details(self):
        return f"Or visit us at our location in {self.location}"

 # create Course subclass that inherits from Course class
class OOP_Course(Course):
     # they have been added as attributes as well but for the purpose of assignment, variable work well.
     # if not okay, please give code examples as to why
     # add values
    description = "OOP Fundamentals"
    trainer = "Mr Anon A. Mouse"
    show_course_id = "#12345"
     # initialize and add attributes
    def __init__(self, description, trainer, show_course_id):
      
      self.description = description
      self.trainer = trainer
      self.show_course_id = show_course_id
      
     # add function to print class and trainer
    def trainer_details(self):
        return f'The section is {self.description} led by {self.trainer}.'

     # add function to print course id
    def course_id_details(self):
        return f'The section id is {self.show_course_id}.'

 # to add detail I added a name
student_1 = Course("Samuel", "Kyte")

 # just to show inheritance I have only pulled from subclass for format
course_1 = f'''
Hello {OOP_Course.fullname(student_1)}

Welcome to "{OOP_Course.name},"

{OOP_Course.trainer_details(OOP_Course)}

{OOP_Course.course_id_details(OOP_Course)}



{OOP_Course.contact_details(OOP_Course)}

{OOP_Course.location_details(OOP_Course)}
'''

 # print out the course_1 object
print(course_1)

 # I was also told my documentation was not great; if you could be more specific as to why that is the case, it would be appreciated! Thank you.