import sys
import re
import itertools

file = open(sys.argv[1])

result = 0

qnt_processed = 1

for line in file:
    springs, sizes = line.split(" ")
    sizes = [int(size) for size in sizes.split(",")]

    number_of_unknown = springs.count("?")
    number_of_damaged = springs.count("#")
    total_size = sum(sizes)

    damaged_remaining = total_size - number_of_damaged

    unknown_positions = [
        index for index in range(len(springs)) if springs[index] == "?"
    ]

    to_permutate = (
        damaged_remaining * "#" + (number_of_unknown - damaged_remaining) * "."
    )

    permutations = set(itertools.permutations(to_permutate, len(to_permutate)))

    qnt_arrangements = 0

    print(f"{round(qnt_processed / 1000 * 100)}%")
    qnt_processed += 1

    print("Permutations:", len(permutations))

    for permutation in permutations:
        current_springs = list(springs)

        for i in range(len(unknown_positions)):
            pos = unknown_positions[i]
            current_springs[pos] = permutation[i]

        matches = re.findall("(#+)", "".join(current_springs))

        if len(matches) == len(sizes):
            if [len(match) for match in matches] == sizes:
                qnt_arrangements += 1

    result += qnt_arrangements

print()
print(result)
