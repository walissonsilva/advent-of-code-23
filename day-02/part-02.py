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

    bigger_blue, bigger_red, bigger_green = 0, 0, 0

    for subset in subsets:
        matches = re.findall("(\d+ blue)|(\d+ red)|(\d+ green)", subset)

        for match in matches:
            blue, red, green = (
                get_number_of_balls(match[0]),
                get_number_of_balls(match[1]),
                get_number_of_balls(match[2]),
            )

            if blue > bigger_blue:
                bigger_blue = blue
            if red > bigger_red:
                bigger_red = red
            if green > bigger_green:
                bigger_green = green

            if blue > 14 or green > 13 or red > 12:
                is_possible = False

    print(
        f"Game {game}:",
        bigger_red,
        bigger_green,
        bigger_blue,
        bigger_green * bigger_red * bigger_blue,
    )

    sum += bigger_green * bigger_red * bigger_blue
    game += 1

print(sum)
