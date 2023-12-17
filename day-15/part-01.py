import sys


file = open(sys.argv[1])

strings = file.readline().replace("\n", "").split(",")

result = 0

for string in strings:
    current_value = 0
    for symbol in string:
        current_value += ord(symbol)
        current_value = current_value * 17 % 256

    result += current_value

print(result)
