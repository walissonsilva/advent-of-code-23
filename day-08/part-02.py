import re
file = open('input.txt')

instruction = file.readline().replace('\n', '')

index = {'R': 1, 'L': 0}

file.readline()

map = {}

for line in file:
    matches = re.findall('\\w+', line)

    map[matches[0]] = [matches[1], matches[2]]


ends_with_a = list(filter(lambda key: key[-1] == 'A', map.keys()))


def get_steps_to_find_z(initial_position):
    instruction_index = 0
    current_value = map[initial_position][index[instruction[instruction_index]]]

    count = 1

    number_of_instructions = len(instruction)

    ends_with_z = []

    while current_value[-1] != 'Z':
        if current_value[-1] == 'Z':
            ends_with_z.append(current_value)

        instruction_index = count % number_of_instructions
        count += 1

        current_instruction_index = index[instruction[instruction_index]]

        current_value = map[current_value][current_instruction_index]

    print(current_value, ends_with_z)
    return count


steps = []
result = 1

for initial_position in ends_with_a:
    print(initial_position)
    qtd_steps = get_steps_to_find_z(initial_position)
    steps.append(qtd_steps)

    result *= qtd_steps

print(steps)
print(int(result))
