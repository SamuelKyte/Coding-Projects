 # I was trying to find a more efficient way to calculate the mean of the list so I imported the statistics package. I learned how to do that here: https://www.geeksforgeeks.org/statistical-functions-python-set-1averages-measure-central-location/
import statistics

 # Create a list location.
num_list = []

 # Create a variable for the loop using a boolean.
num = True

 # Create a while loop because we could potentially enter limitless numbers.
while num:
      num=int(input("\nPlease enter a number (enter '-1' to calculate the avg): \n"))
      num_list.append(num)  # Loop the newly entered variables into the list.
  
      if num == -1:  # Create a break condition and remove that condition from the list.
            num_list.remove(-1)
            print(f' The average of your numbers is {statistics.mean(num_list)}.') # Calculate and print the list
            break