'''I recently got feedback from Tammy-Lee Bastian that was AWESOME about writing multiline code, so for longer comments, per their suggestion, so I will be doing that!

I recieved a piece of code to help at: https://stackoverflow.com/questions/47612009/validating-username-pswd-from-txt-file-in-python-unwanted-looping

I ammended it to my program and changed quite a few things but it taught me to define a function, create a password attempt loop, as well as a few other things that haven't been covered.

I also got a piece of code from a Discord Reviewer with Hyperion Dev named Neil.

The code from Neil was great but definitely needed a lot of tinkering to fit into my program. 

The biggest change was the idea of a global variable within my function: https://discuss.codecademy.com/t/why-cant-i-set-a-global-variable-within-a-function/439339/4
'''

 # First we will design this all within a function called login
def login():
    login = False # We want to assume that the login function is false until proven true.
    password_attempt_loop = 0 # assign a value to our password attempt loop
    while login != True:
        if password_attempt_loop == 3: # create a condition for if the user is wrong 3 times
            print("Sorry entered incorrect password three times. ")
            break # make sure that the function stops working       
        else:
            users = open("user.txt", "r+") # open the user file to access credentials
            global username # MAKE USERNAME A GLOBAL VARIABLE. This comes in handy later.
            username = input("Please enter username: ") # create input for username
            password = input("Please enter password: ") # create input for password
            
            for i in users.readlines(): # create for loop for each line of user info 
                data = i.strip().split(", ") # get rid of any extra stuff
                if username == data[0] and password == data[1]: # index the username and password within data
                    login = True # create condition for login to be true!
                    return login
        print("\nUsername or password is incorrect. \nTry again.\n") # if login is wrong, give an error and reattempt
        password_attempt_loop += 1 # add 1 to password loop to get to max 3 limit
        users.close() # close our user.txt file
    return login

'''Earlier I had written everything within a single function which created a lot of issues. Neil gave me this tip of adding the bulk outside of our original function which allows us a bit more flexibility.'''

login_test = login() # create a variable to assign more details outside of function

while login_test == True: # If we do get that earlier true value for our function:
  if username == "admin": # comptask2 says to make an extra condition for admin(global variable)
    
    # We have our menu with additional admin features
    menu = input('''\nSelect one of the following Options below: 
  r - Registering a user
  a - Adding a task
  va - View all tasks
  vm - View my task
  s - View Statistics
  e - Exit
  : ''').lower() # in lower case if uppercase were entered by user
    
    if menu == 'r': # condition for registration
      reg_user = input("Please enter a username: ") # new username
      reg_pass = input("Please enter a password: ") # new password
      conf_pass = input("Please confirm your password: ") # confirm the password
      new_entry = [] # create a new empty list
      if reg_pass==conf_pass: # if user confirms password correctly:
        new_entry.append(reg_user) # add username to list
        new_entry.append(reg_pass) # add password to list
        new_entry = ', '.join(new_entry) # join them with a comma
        
        with open('user.txt', 'a') as f: # open up user file with AMMEND function. Dont overwrite
          f.write("\n") # make sure its entered on a new line
          f.write(new_entry) # add entry to file
      else:
        print("Passwords do not match. Please try again.") # put in a condition if they couldn't confirm password
        pass # pass brings us back to main menu until user exits

    elif menu == 'a': # Add tasks (I already formatted the tasks data to appear nicer)
      new_task_list = [] # create new empty list
      title_a = input("What is the title of the task: ") # create the title
      new_task_list.append(title_a) # add to list
      who_a = input("What is username of the person whom the task is assigned to: ") # assigned user
      new_task_list.append(who_a) # add to list
      date_a = input("What is the date today (Ex format: 10 Oct 2019): ") # enter today's date
      new_task_list.append(date_a) # add to list
      due_a = input("What is the due date of the task (Ex format: 10 Oct 2019): ") # enter due date
      new_task_list.append(due_a) # add to list
      desc_a = input("Enter a breif description of the task: ") # create description
      new_task_list.append(desc_a) # add to list
      complete = "No" # enter 'no' value for complete
      new_task_list.append(complete) # add to list
      new_task_list = ", ".join(new_task_list) # join list with commas and spaces
  
      with open("tasks.txt", "a") as f: # write as entry into task file
        f.write("\n")
        f.write(new_task_list)
      pass
      
    elif menu == 'va': # view all tasks
      with open("tasks.txt", "r") as f: # read the lines individually and format them nicely
        for line in f:
          line = line.split(", ")
          task = f'''
  Task:             {line[0]}                  
  Assigned to:      {line[1]}                                               
  Date assigned:    {line[2]}                                         
  Due date:         {line[3]}                                        
  Task Description: {line[4]}                                                
  Task Complete?    {line[5]}
                      '''
          print(task)
          pass
          
    elif menu == 'vm': # very similar to 'va', except we will look at the username 
      with open("tasks.txt", "r") as f:
        for line in f:
          line = line.split(", ")
          task = f'''
  Task:             {line[0]}                  
  Assigned to:      {line[1]}                                               
  Date assigned:    {line[2]}                                         
  Due date:         {line[3]}                                        
  Task Description: {line[4]}                                                
  Task Complete?    {line[5]}
                      '''
          if line[1] == username: # again our global variable comes in handy
            print(task)
          elif line[1] !=username:
            print("Currently no more tasks are assigned to this user...\n")
            pass
            
    elif menu == 's': # All we have to do is format the length of the txt files
      with open("user.txt", "r") as f:
        print(f"\nThere are a total of {len(f.readlines())} users within this system.")
        f.close()
      with open("user.txt", "r") as f:
        print(f"\nThere are a total of {len(f.readlines())} assigned tasks.\n")
        f.close()
      pass
      
    elif menu == 'e': # create a program exit
      print("Goodbye!")
      exit()

  else: # Just repeat edited menu but remove 's' and 'r' (see above for comments)
        menu = input('''\nSelect one of the following Options below:
  a - Adding a task
  va - View all tasks
  vm - View my task
  e - Exit
  : ''').lower()
    
        if menu == 'a':
          new_task_list = []
          title_a = input("What is the title of the task: ")
          new_task_list.append(title_a)
          who_a = input("What is username of the person whom the task is assigned to: ")
          new_task_list.append(who_a)
          date_a = input("What is the date today (Ex format: 10 Oct 2019): ")
          new_task_list.append(date_a)
          due_a = input("What is the due date of the task (Ex format: 10 Oct 2019): ")
          new_task_list.append(due_a)
          desc_a = input("Enter a breif description of the task: ")
          new_task_list.append(desc_a)
          complete = "No"
          new_task_list.append(complete)
          new_task_list = ", ".join(new_task_list)
      
          with open("tasks.txt", "a") as f:
            f.write("\n")
            f.write(new_task_list)
          pass
      
        elif menu == 'va':
          with open("tasks.txt", "r") as f:
            for line in f:
              line = line.split(", ")
              task = f'''
      Task:             {line[0]}                  
      Assigned to:      {line[1]}                                               
      Date assigned:    {line[2]}                                         
      Due date:         {line[3]}                                        
      Task Description: {line[4]}                                                
      Task Complete?    {line[5]}
                          '''
              print(task)
              pass
        elif menu == 'vm':
          with open("tasks.txt", "r") as f:
            for line in f:
              line = line.split(", ")
              task = f'''
      Task:             {line[0]}                  
      Assigned to:      {line[1]}                                               
      Date assigned:    {line[2]}                                         
      Due date:         {line[3]}                                        
      Task Description: {line[4]}                                                
      Task Complete?    {line[5]}
                          '''
              if line[1] == username:
                print(task)
              elif line[1] !=username:
                print("Currently no more tasks are assigned to this user...\n")
                pass
              elif menu == 'e':
                print("Goodbye!")
                exit()

'''That's it! This took me THREE DAYS of scraping my brain and scouring the internet and discord for help but finally its finished with hopefully not too many needed improvements...

Incredibly difficult but well worth the effort and feeling of accomplishment. I can't believe I just started coding two weeks ago!'''