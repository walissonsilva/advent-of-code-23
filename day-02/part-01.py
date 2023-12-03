import re

file = open("day-02/input.txt", "r")


def get_number_of_balls(match):
    if not match:
        return 0

    return int(match.split(" ")[0])


game = 1
sum = 0
for line in file:
    subsets = line.split(": ")[1]
    subsets = subsets.split("; ")

    is_possible = True

    for subset in subsets:
        matches = re.findall("(\d+ blue)|(\d+ red)|(\d+ green)", subset)

        for match in matches:
            blue, red, green = (
                get_number_of_balls(match[0]),
                get_number_of_balls(match[1]),
                get_number_of_balls(match[2]),
            )

            if blue > 14 or green > 13 or red > 12:
                is_possible = False

    print(f"Game {game}:", is_possible)
    if is_possible:
        sum += game

    game += 1

print(sum)
