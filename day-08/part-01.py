import re
file = open('input.txt')

instruction = file.readline().replace('\n', '')

index = {'R': 1, 'L': 0}

file.readline()

map = {}

for line in file:
    matches = re.findall('[A-Z]+', line)

    map[matches[0]] = [matches[1], matches[2]]


instruction_index = 0
current_value = map['AAA'][index[instruction[instruction_index]]]

count = 1

number_of_instructions = len(instruction)

while current_value != 'ZZZ':
    instruction_index = count % number_of_instructions
    count += 1

    current_instruction_index = index[instruction[instruction_index]]

    current_value = map[current_value][current_instruction_index]

print(count)
