 # I imported math but personally I think that the stats package is a little more helpful in this program because it holds the median function.
import math
import statistics

 # i just quickly created a while loop to collect my 10 numbers. 
i=0
float_list=[]
while 10>i:
  float_v = input("Please enter a number(whole or decimal): ")
  float_v = float(float_v) # I want to convert my strings into floats before adding them to my list.
  float_list.append(float_v) # now that they are floats I can add them to my list
  i+=1 # each time a number is entered i need to add 1 to i so the loop knows when to break.

# I just printed this to see our list before manipulation
print(float_list)

 # We can use this function to get the sum
total = sum(float_list)
print(total)

 # I got help here for indexing min and max: https://stackoverflow.com/questions/67459407/index-of-max-value-from-list-of-floats-python
max_val = max(float_list)
max_idx = float_list.index(max_val)
print(max_idx)

min_val = min(float_list)
min_idx = float_list.index(min_val)
print(min_idx)

 # This function gives us the average
avg_val = sum(float_list)/len(float_list)
print(round(avg_val,2))

 # and here we have the median, which because we entered 10 numbers, it will always be the middle numbers divided by 2.
med_val = statistics.median(float_list)
print(med_val)