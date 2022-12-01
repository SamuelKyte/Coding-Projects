 # I thought I would do a grid of 5x5, but it could be anything

number_of_rows = 5
number_of_columns = 5

 # create grid of '-'
grid = [["-"] * number_of_columns for _ in range(number_of_rows)]

#add mines
mines=int(input("How many mines would you like in the structure (0-25): "))
if mines > 25 or mines < 0: # dont let user add more mines than matrix
  print("Invalid Selection")
  exit()

 # let user select where mines are placed
 # this could be random too but I thought, why not pick placement
for i in range(mines):
    row_in=int(input("Please enter a number 0-4: "))
    if row_in > 4 or row_in < 0: # only within range
      print("Invalid Selection")
      exit()
    col_in=int(input("Please enter a number 0-4: "))
    if col_in > 4 or col_in < 0:
      print("Invalid Selection")
      exit()
    if grid[row_in][col_in] == '-': # place mine
      grid[row_in][col_in] = "#"
      print("Mine placed.")
      pass
    elif grid[row_in][col_in] == "#": # don't double place mines
      print("Mine has already been placed here.\nThis mine will not be placed.")

for row in grid: # print the grid with '#' and '-'
    print(row)


'''I used and modified some code from: https://www.askpython.com/python/examples/create-minesweeper-using-python for the proximity/adjacency matrix'''
 # replace '-' with 0 so we can add values to it
for r in range(5):
    for col in range(5):
        if grid[r][col] == '-':
            grid[r][col]=0

 # Loop for counting each cell value 
 # n = range of r or col
n = 5
for r in range(5):
    for col in range(5):
        # Skip, if it contains a mine
        if grid[r][col] == "#":
            continue

        # Check up  
        if r > 0 and grid[r-1][col] == "#":
            grid[r][col] = grid[r][col] + 1
        # Check down    
        if r < n-1  and grid[r+1][col] == "#":
            grid[r][col] = grid[r][col] + 1
        # Check left
        if col > 0 and grid[r][col-1] == "#":
            grid[r][col] = grid[r][col] + 1
        # Check right
        if col < n-1 and grid[r][col+1] == "#":
            grid[r][col] = grid[r][col] + 1
        # Check top-left    
        if r > 0 and col > 0 and grid[r-1][col-1] == "#":
            grid[r][col] = grid[r][col] + 1
        # Check top-right
        if r > 0 and col < n-1 and grid[r-1][col+1] == "#":
            grid[r][col] = grid[r][col] + 1
        # Check below-left  
        if r < n-1 and col > 0 and grid[r+1][col-1] == "#":
            grid[r][col] = grid[r][col] + 1
        # Check below-right
        if r < n-1 and col < n-1 and grid[r+1][col+1] == "#":
            grid[r][col] = grid[r][col] + 1

for row in grid: # outer loop for rows
    print(row)
  
""" I DID IT! This was super challenging and fun. It's always exciting to learn something new. As always, please let me know if I can improve anything."""