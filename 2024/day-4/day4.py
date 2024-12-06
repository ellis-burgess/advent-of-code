input = []

with open('input.txt') as f:
  for line in f:
    input.append(line.strip())

xmas_count = 0

# find all the X's
# get 2d coords of each X, make string in every direction of 4 chars and add to maybe_xmas

def find_all_dir_strings(input, row, col):
  potential_matches = []
  if col + 3 < len(input[row]):
    potential_matches.append(''.join([input[row][col], input[row][col+1], input[row][col+2], input[row][col+3]]))
    if row + 3 < len(input):
      potential_matches.append(''.join([input[row][col], input[row+1][col+1], input[row+2][col+2], input[row+3][col+3]]))
    if row - 3 >= 0:
      potential_matches.append(''.join([input[row][col], input[row-1][col+1], input[row-2][col+2], input[row-3][col+3]]))
  
  if col - 3 >= 0:
    potential_matches.append(''.join([input[row][col], input[row][col-1], input[row][col-2], input[row][col-3]]))
    if row + 3 < len(input):
      potential_matches.append(''.join([input[row][col], input[row+1][col-1], input[row+2][col-2], input[row+3][col-3]]))
    if row - 3 >= 0:
      potential_matches.append(''.join([input[row][col], input[row-1][col-1], input[row-2][col-2], input[row-3][col-3]]))
  
  if row + 3 < len(input):
    potential_matches.append(''.join([input[row][col], input[row+1][col], input[row+2][col], input[row+3][col]]))
  if row - 3 >= 0:
    potential_matches.append(''.join([input[row][col], input[row-1][col], input[row-2][col], input[row-3][col]]))
  
  return potential_matches



for row in range(len(input)):
  for col in range(len(input[row])):
    if input[row][col] == "X":
      potentials = find_all_dir_strings(input, row, col)
      # print(row, col, potentials)
      xmas_count += len([s for s in potentials if s == "XMAS"])

print(xmas_count)
