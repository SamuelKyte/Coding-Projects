#context
print("Hello, and congradulations on your completion of the triathlon! \n\nPlease enter your times for each event to see if you qualify for an award. \n")

#create variables for each event
print('What was your time for the running event: ')
run_m = int(input("How many minutes for the running event: "))
run_s = int(input("How many seconds for the running event: "))

run_t = ((run_m*60)+(run_s))

print(' ')
print('What was your time for the swimming event: ')
swim_m = float(input("How many minutes for the swimming event: "))
swim_s = float(input("How many seconds for the swimming event: "))

swim_t = ((swim_m*60)+(swim_s))

print(' ')
print('What was your time for the cycling event: ')
cycle_m = float(input("How many minutes for the cycling event: "))
cycle_s = float(input("How many seconds for the cycling event: "))

cycle_t = ((cycle_m*60)+(cycle_s))

#calculate total time in seconds 
tot_time = (run_t + swim_t + cycle_t)

#I want to display minutes and seconds so we will have to separate the variables
tot_min = int(tot_time/60)

#minutes calculated so now we need remaining seconds for display
tot_sec = int(tot_time - (tot_min*60))

#display total time
print(' ')
print(f'Your total time is {tot_min} minutes and {tot_sec} seconds!')

#display award categories
if tot_min <100 or tot_min ==100 and tot_sec==0:
  print("Congradulations! You qualify for Provincial Colours.")
elif tot_min <105 or tot_min ==105 and tot_sec==0:
  print("Congradulations! You qualify for Provincial Half Colours.")
elif tot_min <110 or tot_min ==110 and tot_sec==0:
  print("Congradulations! You qualify for Provincial Scroll.")
elif tot_min >=110:
  print("Congradulations! Unfortunately you do not qualify for an award. Try again next year.")

#My brain was just not working this morning because that took me way longer than it should have xD