 # Create empty list to store emails
inbox = []

 # create email class
class Email:
   # initialize with 4 attributes
  def __init__(self, from_address, has_been_read, is_spam, contents):
    self.from_address = from_address
    self.has_been_read = has_been_read
    self.is_spam = is_spam
    self.contents = contents

   # I created this function for the purpose of task, although its mostly unused
  def message():
    for email in inbox: # for loop through inbox list
      email = Email(email[0], email[1], email[2], email[3]) # make class objects
       # return formatted class string
      return f'''
        From: {email.from_address}
        Read: {email.has_been_read}
        Spam: {email.is_spam}
        Message: {email.contents}
        '''
   # function to mark emails as read
  def mark_as_read(self):
      for email in inbox: # for loop through inbox
        index = inbox.index(email)+1 # formatted index #
        email_f = Email(email[0], email[1], email[2], email[3]) # class object creation
         # formatted class string
        email = f'''
        {index}  From: {email_f.from_address}
           Read: {email_f.has_been_read}
           Spam: {email_f.is_spam}
           Message: {email_f.contents}
        '''
        print(email)
       # selection input
      select = int(input("Which email would you like to read: "))
      for email_n in inbox: # new for loop
        if select == inbox.index(email_n)+1: # pinpoint selection
            email_n[1] = True # change attribute
            print(email_n) # print it
      

  def mark_as_spam(self): # repeat of mark as read function but for spam attribute
      for email in inbox:
        index = inbox.index(email)+1
        email_f = Email(email[0], email[1], email[2], email[3])
        email = f'''
        {index}  From: {email_f.from_address}
           Read: {email_f.has_been_read}
           Spam: {email_f.is_spam}
           Message: {email_f.contents}
        '''
        print(email)
      select = int(input("Which email would you like to mark as spam: "))
      for email_n in inbox:
          if select == inbox.index(email_n)+1:
                email_n[2] = True
                print(email_n)
        
   # function to send email
  def add_email(self):
    send = input("Address of recipient: ") # address input
    message = input("Your message: ") # message input
    new_email = [send, False, False, message] # new list of variable with defaults
    inbox.append(new_email) # add to inbox list
    for email in inbox: # for loop
        index = inbox.index(email)+1 # formatted index
        email = Email(email[0], email[1], email[2], email[3]) # create class objects
         # print formatted inbox
        email = f'''
        {index}  From: {email.from_address}
           Read: {email.has_been_read}
           Spam: {email.is_spam}
           Message: {email.contents}
        '''
        print(email)
    pass

   # simple count function
  def get_count(self): # print length of inbox list
    print(f"\nYou have {len(inbox)} emails in your inbox.\n")
    pass

   # simple get all emails function
  def get_email(self):
      for email in inbox: # for loop through inbox
        index = inbox.index(email)+1 # formatted index
        email = Email(email[0], email[1], email[2], email[3]) # create class objects
         # print formatted inbox
        email = f'''
        {index}  From: {email.from_address}
           Read: {email.has_been_read}
           Spam: {email.is_spam}
           Message: {email.contents}
        '''
        print(email)

   # get all unread emails
  def get_unread_emails(self):
      for email in inbox: # for loop through inbox
        index = inbox.index(email)+1 # formatted index
        email_f = Email(email[0], email[1], email[2], email[3]) # create class objects
        if email_f.has_been_read==False: # if unread, print
          email = f'''
          {index}  From: {email_f.from_address}
             Read: {email_f.has_been_read}
             Spam: {email_f.is_spam}
             Message: {email_f.contents}
          '''
          print(email)
      pass

   # function is same as get unread email function, except spam attribute
  def get_spam_emails(self):
    for email in inbox:
      email_f = Email(email[0], email[1], email[2], email[3])
      if email_f.is_spam==True:
        index = inbox.index(email)+1
        email = f'''
        {index}  From: {email_f.from_address}
           Read: {email_f.has_been_read}
           Spam: {email_f.is_spam}
           Message: {email_f.contents}
        '''
        print(email)
    pass

   # delete email function
  def delete(self):
    for email in inbox: # for loop through inbox
        index = inbox.index(email)+1 # formatted index
        email = Email(email[0], email[1], email[2], email[3]) # class object creation
         # print all formatted emails
        email = f'''
        {index}  From: {email.from_address}
           Read: {email.has_been_read}
           Spam: {email.is_spam}
           Message: {email.contents}
        '''
        print(email)
     # input selection
    select = int(input("Which email would you like to delete: "))
    for email in inbox: # another for loop
        index = inbox.index(email)+1 # formatted index 
        if select == index: # if selection, remove the email from inbox list
            inbox.remove(inbox[select-1])
        pass

 # I just added three random tuples to fit Email class attribute format
em_1 = 'skyte@cord.edu', False, False, "hi"
em_1 = list(em_1) # convert to lists
em_2 = 'skyte@cord.edu', False, False, "hey"
em_2 = list(em_2)
em_3 = 'skyte@cord.edu', False, False, "sup"
em_3 = list(em_3)
inbox.append(em_1) # add to our empty inbox list
inbox.append(em_2)
inbox.append(em_3)

 # choice variable
sp_user_choice = ""
while sp_user_choice != "quit": # while loop
     # create a menu with input options
    sp_user_choice = input('''
What would you like to do:
    
ga - get all
gu - get unread
gs - get spam
mr - mark read
ms - mark spam
c  - count
d  - delete
s  - send
q  - quit 
    
Selection: ''').lower() # lower case for error handling
     # menu selection conditions and functions
    if sp_user_choice == "ga":
        Email.get_email(Email)
        pass
    elif sp_user_choice == "gu":
        Email.get_unread_emails(Email)
        pass
    elif sp_user_choice == "gs":
        Email.get_spam_emails(Email)
        pass
    elif sp_user_choice == "mr":
        Email.mark_as_read(Email)
        pass #Place your logic here
    elif sp_user_choice == "ms":
        Email.mark_as_spam(Email)
        pass #Place your logic here
    elif sp_user_choice == "c":
        Email.get_count(Email)
    elif sp_user_choice == "d":
        Email.delete(Email)
        pass
    elif sp_user_choice == "s":
        Email.add_email(Email)
        pass #Place your logic here
    elif sp_user_choice == "q":
        print("\nGoodbye")
        exit()
    else:
        print("Oops - incorrect input")

'''
This assignment was a little hard to follow when emails were not given and the idea of sending and recieving emails without text files for in and out seems strange but here is my effort.'''