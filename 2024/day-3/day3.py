inputs_list = []

with open('input.txt') as f:
  for line in f:
    inputs_list.append(line.strip())

inputs = "".join(inputs_list)

# go through the input string; if I hit "don't()" then ignore all characters until I hit "do()"
prev_buffer = ['', '', '', '', '', '', '']
p2_inputs = []
read = True
for c in inputs:
  if ''.join(prev_buffer) == "don't()":
    read = False
  elif ''.join(prev_buffer).endswith("do()"):
    read = True
  
  if read:
    p2_inputs.append(c)
  
  prev_buffer = [prev_buffer[i+1] for i in range(len(prev_buffer)-1)]
  prev_buffer.append(c)

p2_inputs = ''.join(p2_inputs)

def parse_input(inputs):
  inputs = inputs.split("mul(")
  inputs = [i.split(")")[0].split(",") for i in inputs]
  inputs = [i for i in inputs if i[0].isnumeric() and i[1].isnumeric() and len(i) == 2]
  return inputs

sum_p1 = 0
sum_p2 = 0

p1_inputs = parse_input(inputs)
p2_inputs = parse_input(p2_inputs)

for i in p1_inputs:
  sum_p1 += int(i[0]) * int(i[1])

for i in p2_inputs:
  sum_p2 += int(i[0]) * int(i[1])

print(sum_p1, sum_p2)