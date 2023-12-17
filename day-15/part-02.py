import sys
import re

file = open(sys.argv[1])

strings = file.readline().replace("\n", "").split(",")
boxes = {}

result = 0

for string in strings:
    current_value = 0

    label = re.findall("[a-zA-Z]+", string)
    label = label[0]

    for symbol in label:
        current_value += ord(symbol)
        current_value = current_value * 17 % 256

    box = current_value

    operation = string[len(label)]

    if operation == "=":
        length = re.findall("\\d+", string)[0]

        if box not in boxes:
            boxes[box] = {label: length}
        else:
            boxes[box][label] = length
    else:
        for box_content in boxes.values():
            if label in box_content:
                try:
                    del box_content[label]
                except:
                    pass

for box_key, box_content in boxes.items():
    slot_position = 1
    for lens in box_content.values():
        result += (box_key + 1) * int(lens) * slot_position
        slot_position += 1

print(result)
