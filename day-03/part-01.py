
file = open('input.txt')

mtx = []


def check_position(i, j):
    try:
        return not mtx[i][j].isdigit() and mtx[i][j] != '.'
    except:
        return False


def check_is_part_digit(i, j):
    if check_position(i+1, j) or check_position(i-1, j) or check_position(i, j+1) or check_position(i, j-1) or check_position(i+1, j+1) or check_position(i+1, j-1) or check_position(i-1, j-1) or check_position(i-1, j+1):
        return True

    return False


for line in file:
    line_list = [letter for letter in line if letter != '\n']

    mtx.append(line_list)

sum = 0
current_digit = ''
is_part_number = False

for i in range(len(mtx)):
    if current_digit != '' and is_part_number:
        sum += int(current_digit)

    current_digit = ''
    is_part_number = False

    for j in range(len(mtx[i])):
        char = mtx[i][j]
        if char.isdigit():
            current_digit += char
            is_part_number = is_part_number or check_is_part_digit(i, j)
        else:
            if current_digit != '':
                print(current_digit, is_part_number)

            if current_digit != '' and is_part_number:
                sum += int(current_digit)

            current_digit = ''
            is_part_number = False

print(sum)
