import re

file = open('input.txt')

first_line = file.readline()
desired_seeds = [int(seed) for seed in re.findall('\\d+', first_line)]

file.readline()

current_line = file.readline()

relations = {}

while current_line:
    source_destination = current_line.split(' ')[0]

    current_line = file.readline()

    map = {}

    while current_line != '\n' and current_line:
        destination, source, step = [int(value)
                                     for value in current_line.split(' ')]
        map[(source, source + step)] = (destination, destination + step)

        current_line = file.readline()

    relations[source_destination] = map

    current_line = file.readline()


def get_relation(source, current_relations):
    for source_range, destination_range in current_relations.items():
        source_range_start, source_range_end = source_range
        destination_range_start, _ = destination_range
        if source >= source_range_start and source < source_range_end:
            diff = source - source_range_start
            return destination_range_start + diff

    return source


result = -1

for seed in desired_seeds:
    destination = seed
    for key, value in relations.items():
        source = destination

        destination = get_relation(source, value)

    if result == -1 or destination < result:
        result = destination

print(result)
