sample_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# go through the input string; if I hit "don't()" then ignore all characters until I hit "do()"
prev_buffer = ['', '', '', '', '', '', '']
inputs = []
read = True
for c in sample_input:
  if ''.join(prev_buffer) == "don't()":
    read = False
  elif ''.join(prev_buffer).endswith("do()"):
    read = True
  
  if read:
    inputs.append(c)
  
  prev_buffer = [prev_buffer[i+1] for i in range(len(prev_buffer)-1)]
  prev_buffer.append(c)

inputs = ''.join(inputs)
inputs = inputs.split("mul(")
inputs = [i.split(")")[0].split(",") for i in inputs]
inputs = [i for i in inputs if i[0].isnumeric() and i[1].isnumeric() and len(i) == 2]

sum = 0
for i in inputs:
  sum += int(i[0]) * int(i[1])

print(inputs)
print(sum)