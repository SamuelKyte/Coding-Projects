 # NOTE: This task is actually very similar to the first compulsory task in this lesson (L01T18, CT01) so I copied a lot of the code and format from that previous assignment. I just don't want to be mistaken for self plagiarism.

 # First I'll create a variable to ask how many numbers will be sorted in the first list:
num_one = input("How many numbers do you have: ")

 # Then for the for loop we need that variable to be an int so that we can use its length for the for loop:
num_one = int(num_one)

 # Now we need an empty list so that the for loop can give us all of the numbers in one place.
num_one_list = []

 # We also need another empty list to hold all of our numbers. This will come in handy later.

# Now we create that for loop:
for i in range(num_one):
        x = int(input("Please enter your number: ")) # To sort the numbers numerically and not alphabically, we need to ensure that the 'x' entered is listed as an int not a str.
        num_one_list.append(x) # Every entry will be sent to our empty list that we established above.

 # Now we need to sort those numbers.
num_one_list.sort()

 # Now that we have all of our perfectly sorted int's, we need to revert them back to str's so that they can be joined and exported properly. I was not aware of the map() function, but i found it here: https://www.geeksforgeeks.org/python-program-to-convert-list-of-integer-to-list-of-string/
num_one_list = map(str, num_one_list)

 # A list cannot be written to a .txt file so we have to join our list using new line spacing before we can export the data.
num_one_list = "\n".join(num_one_list)

 # Finally we can open up our newly written .txt file, upload our data and close it up. I added a line of text as well just so that later when we read the exported data it looks a little clearer.
with open('numbers1.txt', 'w') as f:
        f.write("List One Numbers:\n")
        f.write(num_one_list)
        f.close()

 # Now that our first .txt file is written, lets repeat that process again to create that second .txt file
num_two = input("How many numbers do you have: ")

num_two = int(num_two)

num_two_list = []

for i in range(num_two):
        y = int(input("Please enter your number: "))
        num_two_list.append(y)

num_two_list.sort()

num_two_list = map(str, num_two_list)

num_two_list = "\n".join(num_two_list)

with open('numbers2.txt', 'w') as f:
        f.write("List Two Numbers:\n")
        f.write(num_two_list)
        f.close()

 # Finally, now that we have our two .txt files (numbers1.txt & numbers2.txt), we can create our third .txt file to sort all of those numbers into one single sorted folder.

 # For confusion with how to read two files and write a new one through merging data, I found help here: https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/

 # We write this piece to merge the two data sets from the .txt files into an empty space.
data = data2 = ""
  
# Reading data from numbers1.txt. We skip line 1 because that's the title.
with open('numbers1.txt') as fp:
    data = fp.readlines()[1:]
    fp.close()
# Reading data from numbers2.txt. We skip line 1 because that's the title.
with open('numbers2.txt') as fp:
    data2 = fp.readlines()[1:]
    fp.close()
# Merge the two files
data += data2

 # Now we have string lists with all of these '\n' areas we need to strip. Then we need to convert the lists to int lists in order to sort them again. I found help here: https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/ and here: https://stackoverflow.com/questions/41494191/strip-a-list-in-python
data = [i.strip('\n') for i in data]
data = [int(i) for i in data]

 # Finally we sort our data, convert them back into string lists, and join them into a nice string for our final .txt file.
data.sort()
data = map(str, data)
data = "\n".join(data)

 # Here is our final product.
with open ('all_numbers.txt', 'w') as fp:
    fp.write("All Numbers:\n")
    fp.write(data)
    fp.close()