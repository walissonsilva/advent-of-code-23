import numpy as np

file = open('input.txt')

mtx = []

for line in file:
    line_list = [symbol for symbol in line if symbol != '\n']

    if '#' not in line_list:
        mtx.append(line_list)

    mtx.append(line_list)

mtx = np.array(mtx)

for line in mtx:
    print(line)

col_index = 0

while col_index < len(mtx[0]):
    column = mtx[:, col_index]
    if '#' not in mtx[:, col_index]:
        print(col_index)
        mtx = np.insert(mtx, col_index, column, axis=1)

        col_index += 1

    col_index += 1

where_galaxies = np.where(mtx == '#')
galaxies_position = list(zip(where_galaxies[0], where_galaxies[1]))


sum = 0
for source_index in range(len(galaxies_position)):
    for destination_index in range(len(galaxies_position)):
        source, destination = galaxies_position[source_index], galaxies_position[destination_index]
        if destination_index > source_index:
            distance = abs(source[0] - destination[0]) + \
                abs(source[1] - destination[1])
            print(source_index + 1, destination_index + 1, distance)
            sum += distance

print(sum)
