
file = open('input.txt')

mtx = []


def check_position(i, j):
    try:
        if not mtx[i][j].isdigit() and mtx[i][j] != '.':
            return [(i, j), mtx[i][j]]

        return []
    except:
        return []


def get_adjacents(i, j):
    adjancents = [check_position(i+1, j) + check_position(i-1, j) + check_position(i, j+1) + check_position(
        i, j-1) + check_position(i+1, j+1) + check_position(i+1, j-1) + check_position(i-1, j-1) + check_position(i-1, j+1)]
    return [adjancent for adjancent in adjancents if len(adjancent)]


for line in file:
    line_list = [letter for letter in line if letter != '\n']

    mtx.append(line_list)

soma = 0
current_digit = ''
adjancents = []
possible_gears = {}

for i in range(len(mtx)):
    if current_digit != '' and len(adjancents):
        adjancent_chars = [adjancent[1] for adjancent in adjancents]
        try:
            adj_index = adjancent_chars.index('*')
            position = adjancents[adj_index][0]

            try:
                possible_gears[position].append(int(current_digit))
            except:
                possible_gears[position] = [int(current_digit)]
        except:
            pass

    current_digit = ''
    adjancents = []

    for j in range(len(mtx[i])):
        char = mtx[i][j]
        if char.isdigit():
            current_digit += char
            adjancents += get_adjacents(i, j)
        else:
            if current_digit != '' and len(adjancents):
                adjancent_chars = [adjancent[1] for adjancent in adjancents]
                try:
                    adj_index = adjancent_chars.index('*')
                    position = adjancents[adj_index][0]

                    try:
                        possible_gears[position].append(int(current_digit))
                    except:
                        possible_gears[position] = [int(
                            current_digit)]
                except:
                    pass

            current_digit = ''
            adjancents = []

print(possible_gears)

for gear in possible_gears.values():
    if len(gear) == 2:
        soma += gear[0] * gear[1]

print(soma)
