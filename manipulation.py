str_manip = (input("Please enter a sentence: "))
#I wanted to learn how to exclude certain characters from the len function: https://stackoverflow.com/questions/19669001/using-len-for-text-but-discarding-spaces-in-the-count
print(f'There are {len(str_manip) - str_manip.count(" ") - str_manip.count(".")} characters in your sentence "{str_manip}"')
print(' ')
print(str_manip[-1])
print(' ')
for i in str_manip[-1]:
  print(str_manip.replace( i, '@'))
print(' ')
print(str_manip[-1] + str_manip[-2] + str_manip[-3])
print(' ')
print(str_manip[0:4] + str_manip[-2] + str_manip[-1])
print(' ')
print(str_manip.replace(' ', '\n'))