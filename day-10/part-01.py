file = open('example1.txt')

mtx = []

max_depth = -1
depths = []


def backtracking(x, y, depth=0):
    if x < 0 or x >= len(mtx) or y < 0 or y >= len(mtx[0]):
        return

    if depths[x][y]:
        if depth > depths[x][y]:
            depths[x][y] = depth
        return

    depths[x][y] = depth

    # if max_depth < depth:
    #     max_depth = depth
    #

    if x + 1 < len(mtx) and mtx[x + 1][y] == 'J':
        backtracking(x + 1, y - 2, depth + 2)
    if x + 1 < len(mtx) and mtx[x + 1][y] == 'L':
        backtracking(x + 1, y + 2, depth + 2)
    if x + 1 < len(mtx) and mtx[x + 1][y] == '|':
        backtracking(x + 2, y, depth + 2)
    if x - 1 >= 0 and mtx[x - 1][y] == '|':
        backtracking(x - 2, y, depth + 2)
    if x - 1 >= 0 and mtx[x - 1][y] == '7':
        backtracking(x - 1, y - 1, depth + 2)
    if x - 1 >= 0 and mtx[x - 1][y] == 'F':
        backtracking(x - 1, y + 1, depth + 2)
    if y + 1 < len(mtx[0]) and mtx[x][y + 1] == '-':
        backtracking(x, y + 2, depth + 2)
    if y + 1 < len(mtx[0]) and mtx[x][y + 1] == '7':
        backtracking(x + 1, y + 1, depth + 2)
    if y - 1 >= 0 and mtx[x][y - 1] == '-':
        backtracking(x, y - 2, depth + 1)
    if y - 1 >= 0 and mtx[x][y - 1] == 'F':
        backtracking(x + 1, y - 1, depth + 1)
    if y - 1 >= 0 and mtx[x][y - 1] == 'L':
        backtracking(x - 1, y - 1, depth + 1)

    return max_depth


line_index = 0

for line in file:
    line_list = [el for el in line if el != '\n']

    mtx.append(line_list)
    depths.append([0 for el in line_list])
    if 'S' in line_list:
        start_position = line_index, line_list.index('S')

    line_index += 1

result = backtracking(*start_position)

print(depths)

print(result)
