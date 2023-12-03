import re

file = open("day-01/input.txt")

map_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

calibration_sum = 0

for line in file:
    calibration = []
    for char in line:
        matches = re.findall(
            "(\d)|(?=(one))|(?=(two))|(?=(three))|(?=(four))|(?=(five))|(?=(six))|(?=(seven))|(?=(eight))|(?=(nine))",
            line,
        )

        matches = [list(match) for match in matches]

        for match in matches:
            m = [m for m in match if m]

            calibration.extend(n if n.isdigit() else map_digit[n] for n in m)

    print(line, m, int(calibration[0] + calibration[-1]), matches)
    calibration_sum += int(calibration[0] + calibration[-1])

print(calibration_sum)
