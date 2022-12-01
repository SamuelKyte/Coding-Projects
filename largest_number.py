'''This task also seems quite easy, so I will solve it in two different ways. To find the largest number within a function we can use the max() function or an indexed sort() function(as well as a variety of other methods as well).

For the second function, I use reverse sort because it is cleaner that trying to find max index# in unknown list.'''

def largest_num1(nums): # define function
  return max(nums) # return max

def largest_num2(nums): # define function
  nums.sort(reverse=True) # sort w/ reverse 
  return nums[0] # return largest # in sorted list

print(largest_num1([1,2,3,4,5,6,7,8,9]))
print(largest_num2([1,2,3,4,5,6,7,8,9]))