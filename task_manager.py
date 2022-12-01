 # import packages
import datetime
import fileinput
import sys

'''Because this capstone is a continuation of L01T19, I have copied all of the relevant code and comments from that assignment.'''

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

 # This function will come in handy later withing the reg_user()
def check(name):
    file = open("user.txt", "r+") # open user file
    users = dict() # create an empty dictionary
    for i in file.readlines(): # create for loop for each line of user info 
        data = i.strip().split(", ") # get rid of any extra stuff
        users[data[0]] = ""
    return (name in users) # returns boolean

def reg_user():
  #reg_user = input("Please enter a username: ") # new username
  
  #if check(reg_user) == True:
  #  print("Username already in use.\n")
  #  pass
  reg_user = input("Please enter a username: ")
  while check(reg_user):
    print("Username already in use.\n")
    reg_user = input("Please enter a username: ")
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
    return reg_user

def add_task():
  new_task_list = [] # create new empty list
  
  with open("tasks.txt", "r") as f:
    x = len(f.readlines())
  task_no = str(x+1)
  new_task_list.append(task_no)
  title_a = input("What is the title of the task: ") # create the title
  new_task_list.append(title_a) # add to list
  who_a = input("What is username of the person whom the task is assigned to: ") # assigned user
  new_task_list.append(who_a) # add to list
  date_a = x = str(datetime.datetime.now()) # enter today's date
  new_task_list.append(date_a) # add to list
  due_a = input("What is the due date of the task (Ex format: YYYY-MM-DD): ") # enter due date
  new_task_list.append(due_a) # add to list
  desc_a = input("Enter a breif description of the task: ") # create description
  new_task_list.append(desc_a) # add to list
  complete = "No" # enter 'no' value for complete
  new_task_list.append(complete) # add to list
  new_task_list = ", ".join(new_task_list) # join list with commas and spaces


  with open("tasks.txt", "a") as f: # write as entry into task file
    f.write("\n" + new_task_list)
    return add_task

def view_all():
   with open("tasks.txt", "r") as f: # read the lines individually and format them nicely
        for line in f:
          line = line.split(", ")
          task = f'''
  Task No:          {line[0]}
  Task:             {line[1]}                  
  Assigned to:      {line[2]}                                               
  Date assigned:    {line[3]}                                         
  Due date:         {line[4]}                                        
  Task Description: {line[5]}                                                
  Task Complete?    {line[6]}
                      '''
          print(task)
        return view_all
          
def view_mine():
#receive the menu and the username currently logged in 
    task_count = 0  # task number
    
    for key in tasks_dict:
    
      task_count += 1 
    
      if username == (tasks_dict[key][2]):  # only view tasks with username
        
        print(f"""
    
    Task {str(task_count)}:    
    
    Task:                      {str(tasks_dict[key][1])}
    
    Assigned to:               {str(tasks_dict[key][2])}
    
    Date assigned:             {str(tasks_dict[key][3])}
    
    Due Date:                  {str(tasks_dict[key][4])}
    
    Task Description:          {str(tasks_dict[key][5])}
    
    Task Complete?             {str(tasks_dict[key][6])}""") 
    
        # select task    
    task_selection = int(input("\nPlease select a task by number to edit (e.g. 1, 2, 3) or type -1 to return to the main menu. \n"))

    if task_selection != -1:  # option to return to menu
        option = input("Would you like to mark the task as complete or edit the task? (e.g. mark OR edit) \n")
        if option == "mark": # mark task as complete
            tasks_dict[task_selection][6] = "Yes" # editing the dictionaries Task selection is your task count, its the key we use to grab our value
            return("Your task has been successfully marked as complete.")
        elif option == "edit": # edit choice, only allowed if not complete
            if tasks_dict[task_selection][6] == "Yes":
              return("Completed tasks cannot be edited")
            else:
              edit_sel = input("Would you like to edit assigned user(u) or due date(d): ").lower()
              if edit_sel == "u":
                n_user = input("Who is the new assigned user: ") # change user
                tasks_dict[task_selection][2]= n_user
                return("The assigned user has been successfully changed.")
                
              elif edit_sel == "d":
                n_due = input("What is the new due date (eg. YYYY-MM-DD): ") # change date
                tasks_dict[task_selection][4]= n_due
                return("The due date has been successfully changed.")
              else:
                return("Invalid Selection") # in case invalid option

 # this is the stats function
def analysis():
  with open("user.txt", "r") as f: # open user txt file
        print(f"\nThere are a total of {len(f.readlines())} users within this system.") # print # of users
        f.close()
  with open("tasks.txt", "r") as f: # open tasks txt file
    print(f"\nThere are a total of {len(f.readlines())} assigned tasks.\n") # print # of tasks
    f.close()
  return analysis

def terminate(): # create a program exit
  print("Goodbye!")
  exit()
  return terminate

 # generate reports function

def task_over(): # task overview portion of gen reports
    with open("task_overview.txt", "w") as f: # open new file to write
        with open("tasks.txt", "r+") as f2: # read tasks txt file
            x = len(f2.readlines()) # print length of tasks file / # of tasks
            with open("task_overview.txt", "w") as f: # for next portion it had to be done seperately
                with open("tasks.txt", "r+") as f2: # open both files again
                    count = 0 # count # 
                    count_c = 0 # count completed tasks
                    count_u = 0 # count incomplete tasks
                    count_o = 0 # count overdue tasks
                    count_d = 0 # count incomplete and overdue
                    for line in f2: # get counter
                        newline = line.rstrip('\n')   # remove the white spaces on the sides
                        split_line = newline.split(", ") # split
                        tasks_dict[count] = split_line # key value pairs.Notice that your key is the task
                        count += 1
                      
                    for task in tasks_dict.values(): # open dictionary
                          due_date = int(task[4].replace("-", "")) # take hyphens out of date
                          if task[6] == "Yes": # if complete count
                            count_c += 1
                          elif task[6] == "No": # if incomplete count
                            count_u += 1
                          if due_date < int(datetime.date.today().strftime("%Y%m%d")): # compare due date ints for larger value & count
                            count_o += 1
                          if task[6] == "No" and due_date < int(datetime.date.today().strftime("%Y%m%d")): # count incomplete and overdue
                            count_d += 1
                    try:
                         # write all lines to new taskoverview txt file
                        f.write(f'There are a total of {str(x)} tasks in the system.\n')
                        f.write(f'There are a total of {str(count_c)} completed tasks in the system.\n') #oops
                        f.write(f'There are {str(count_d)} tasks that are incomplete and overdue.\n')
                        f.write(f'{str((count_u/count)*100)}% of the tasks are incomplete.\n')
                        f.write(f'There are {str(count_u)} incomplete tasks in the system.\n')
                        f.write(f'{str((count_o/x)*100)}% of the tasks are overdue.\n')#oops
                    except ZeroDivisionError as e:
                        print(e)
                        return
    with open("task_overview.txt", "r") as f: # print txt lines for user readability
        print("\n")
        for line in f:
          print(line)

def user_over(): # 2nd portion of gen reports

    # user overview portion        
    with open("user.txt", "r+") as f2: # open user file
        with open("tasks.txt", "r+") as f3: # open tasks file
            x = len(f2.readlines()) # read length of user file
            y = len(f3.readlines()) # read length of tasks file
            with open("user_overview.txt", "w") as f: # open new file to write
                f.write(f'There are a total of {str(x)} users in the system.\n') # write file length
                f.write(f'There are a total of {str(y)} tasks in the system.\n') # write file length
    with open("user.txt", "r+") as f2: # open user file
        with open("tasks.txt", "r+") as f3: # open tasks file
            users = [] # empty list for usernames
            for line in f2:
              newline = line.rstrip('\n')   # remove the white spaces on the sides
              split_line = newline.split(", ") # format
              users.append(split_line[0]) # add usernames to list
              with open("user_overview.txt", "w") as f: # open new file to write
                for user in users: # 
                    counter = 0
                    counter_c = 0
                    counter_i = 0
                    counter_o = 0
                    for task in tasks_dict.values(): # count items according to user
                        due_date = int(task[4].replace("-", ""))
                        if str(task[2]) == str(user):
                          counter += 1
                        if task[2] == user and task[6] == "Yes":
                          counter_c += 1
                        if task[2] == user and task[6] == "No":
                          counter_i += 1
                        if task[2] == user and task[6] == "No" and due_date < int(datetime.date.today().strftime("%Y%m%d")):
                          counter_o += 1
            
                       # write lines to txt file
                    try:
                        for user in users:
                            f.write(f"{str((counter_c/counter)*100)}% of {user}'s tasks are completed.\n")
                            f.write(f"{str((counter_i/counter)*100)}% of {user}'s tasks are incomplete.\n")
                            f.write(f"{str((counter_o/counter)*100)}% of {user}'s tasks are incomplete and overdue.\n")
                            f.write(f'{user} has {str(counter)} tasks assigned to them.\n')
                            f.write(f'{user} has {str((counter/y)*100)}% of the total tasks assigned to them.\n\n') 
                    except ZeroDivisionError as e:
                        print(e)
    with open("user_overview.txt", "r") as f: # print lines for user on screen
        print("\n")
        for line in f:
            print(line)  
        print("\n")  

login_test = login() # create a variable to assign more details outside of function

while login_test == True: # If we do get that earlier true value for our function:
  tasks_dict = {} # empty dict

  # store all tasks in dict
  count = 1

  with open("tasks.txt", "r+") as f2: # 
     for line in f2:  
        newline = line.rstrip('\n')   # remove the white spaces on the sides
        split_line = newline.split(", ")
        tasks_dict[count] = split_line # key value pairs.Notice that your key is the task
        count += 1
       
  if username == "admin": # comptask2 says to make an extra condition for admin(global variable)
    # We have our menu with additional admin features
    menu = input('''\nSelect one of the following Options below: 
  r - Registering a user
  a - Adding a task
  va - View all tasks
  vm - View my task
  s - View Statistics
  gr - Generate Reports
  e - Exit
  : ''').lower() # in lower case if uppercase were entered by user
    
    if menu == 'r': # condition for registration
      reg_user()
      pass # pass brings us back to main menu until user exits

    elif menu == 'a': # Add tasks (I already formatted the tasks data to appear nicer)
      add_task()
      pass
      
    elif menu == 'va': # view all tasks
      view_all()
      pass
          
    elif menu == 'vm': # very similar to 'va', except we will look at the username 
      view_mine()
      with open("tasks.txt", "r+") as f2: # update tasks.txt
          for val in tasks_dict.values(): # join dict values
              val = ', '.join(val)
              f2.write(val + "\n") # write to file
      pass
            
    elif menu == 's': # All we have to do is format the length of the txt files
      analysis()
      pass
      
    elif menu == 'gr': # generate reports (seperated into two functions)
      task_over()
      user_over()
      pass  
    elif menu == 'e': # create a program exit
      terminate()

  else: # Just repeat edited menu but remove 's', 'r', and 'gr' (see above for comments)
        menu = input('''\nSelect one of the following Options below:
  a - Adding a task
  va - View all tasks
  vm - View my task
  e - Exit
  : ''').lower()
    
        if menu == 'a':
          add_task()
          pass
      
        elif menu == 'va':
          view_all()
          pass
          
        elif menu == 'vm':
          view_mine()
          with open("tasks.txt", "r+") as f2:
              for val in tasks_dict.values():
                  print(val)
                  val = ', '.join(val)
                  print(val)
                  f2.write(val + "\n")
          pass
          
        elif menu == 'e':
          terminate()
