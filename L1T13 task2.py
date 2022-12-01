#for some reason this task was particularly complicated for me and I couldn't figure it out! I googled the answer to try to work backwards and now it makes a lot more sense. I think I was trying to over complicate it...
#I found help here: https://stackoverflow.com/questions/59699347/for-loop-leap-year-input

#prompt user to enter a starting year
start_year = int(input("Please enter the year you would like to start checking leap years from: "))

#prompt user to enter amount of years they want to check
total_years = int(input("Please enter over how many years you would like to check: ")) 

#set paramenters for range that will be checked
for year in range(start_year, start_year + total_years):
  #check divisibility by 4 (if its a leap year)
  if year % 4 == 0:       
    print(f"{year} is a leap year.") 
  else:
    print (f"{year} is not a leap year.")