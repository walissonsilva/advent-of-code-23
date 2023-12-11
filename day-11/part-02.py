import numpy as np
import copy

file = open('input.txt')

mtx = []

for line in file:
    line_list = [symbol for symbol in line if symbol != '\n']

    mtx.append(line_list)

mtx = np.array(mtx)

where_galaxies = np.where(mtx == '#')
galaxies = [[galaxy[0], galaxy[1]]
            for galaxy in zip(where_galaxies[0], where_galaxies[1])]

galaxies_position = copy.deepcopy(galaxies)

for r in range(len(mtx)):
    if '#' not in mtx[r]:
        for g in range(len(galaxies)):
            if galaxies[g][0] > r:
                galaxies_position[g][0] += 1000000 - 1


for c in range(len(mtx[0])):
    if '#' not in mtx[:, c]:
        for g in range(len(galaxies)):
            if galaxies[g][1] > c:
                galaxies_position[g][1] += 1000000 - 1

col_index = 0

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
