import sys
import re
import itertools

file = open(sys.argv[1])

result = 0

qnt_processed = 1


def isNotValid(damaged_matches, sizes):
    if len(damaged_matches) > len(sizes):
        return True

    return False


def isValid(damaged_matches, sizes):
    if len(damaged_matches) == len(sizes):
        if [len(match) for match in damaged_matches] == sizes:
            return True

    return False


def recursion(springs, sizes):
    damaged_matches = re.findall("(#+)", springs)

    if isValid(damaged_matches, sizes):
        return 1

    replaced_with_damaged = springs.replace("?", "#", 1)

    if replaced_with_damaged == springs:
        return 0

    return recursion(replaced_with_damaged, sizes) + recursion(
        springs.replace("?", ".", 1), sizes
    )


result = 0

for line in file:
    springs, sizes = line.split(" ")
    sizes = [int(size) for size in sizes.split(",")]

    arrangements = recursion(springs, sizes)
    # print(arrangements)
    result += arrangements

print(result)
