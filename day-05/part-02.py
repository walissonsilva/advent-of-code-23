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


def get_relation(source, relation_key):
    next_change = 0
    current_relations = relations[relation_key]

    for source_range, destination_range in current_relations.items():
        source_range_start, source_range_end = source_range
        destination_range_start, _ = destination_range
        if source >= source_range_start and source < source_range_end:
            diff = source - source_range_start
            next_change = source_range_end - source

            return destination_range_start + diff, next_change
        else:
            distance = source_range_start - \
                source if source < source_range_start else source - source_range_end
            if next_change == 0 or next_change < distance:
                next_change = distance

    return source, next_change


result = -1


def get_location(seed):
    destination = seed
    next_near_change = 0
    for key, value in relations.items():
        source = destination

        destination, next_change = get_relation(source, key)

        if next_near_change == 0 or next_change < next_near_change:
            next_near_change = next_change

    return destination, next_near_change


for i in range(0, len(desired_seeds), 2):
    seed_start, seed_end = desired_seeds[i], desired_seeds[i] + \
        desired_seeds[i + 1]

    print(f'Analyzing {desired_seeds[i + 1]} seeds..')

    seed = seed_start
    while seed <= seed_end:
        location = 0
        location, next_change = get_location(seed)
        if result == -1 or location < result:
            result = location

        seed += next_change


print(result)
