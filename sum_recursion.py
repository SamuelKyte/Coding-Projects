'''Please let me know if I am incorrect, but this task seemed really simple!'''

 # First define your function
def recur_sum(nums, index): # should include 2 parameters (list, index)
    return sum(nums[0:index+1]) # we want to include the index number itself so add 1

 # print our function with both arguements
print(recur_sum([1,4,5,3,12,16], 4))
print(recur_sum([1,4,7,9], 2))
print(recur_sum([1,4,7,9], 3))