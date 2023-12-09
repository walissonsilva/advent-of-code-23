import re

file = open('example.txt')

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
    current_relations = relations[relation_key]

    for source_range, destination_range in current_relations.items():
        source_range_start, source_range_end = source_range
        destination_range_start, _ = destination_range
        if source >= source_range_start and source < source_range_end:
            diff = source - source_range_start
            return destination_range_start + diff

    return source


result = -1


def get_location(seed):
    destination = seed
    for key, value in relations.items():
        source = destination

        destination = get_relation(source, key)

    return destination


for i in range(0, len(desired_seeds), 2):
    seed_start, seed_end = desired_seeds[i], desired_seeds[i] + \
        desired_seeds[i + 1]

    print(f'Analyzing {desired_seeds[i + 1]} seeds..')

    for seed in range(seed_start, seed_end):
        location = 0
        try:
            location = seed_memo[seed]
        except:
            location = get_location(seed)
            seed_memo[seed] = location
        finally:
            print(seed, location)
            input()
            if result == -1 or location < result:
                result = location


print(result)
