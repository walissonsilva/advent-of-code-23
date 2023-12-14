import numpy as np

file = open("input.txt")

grid = []

for line in file:
    grid.append(list(line.replace("\n", "")))


grid = np.array(grid)

height = len(grid)

matches_line = [
    np.where(grid[i] == "#")[0].tolist() + [height] for i in range(len(grid))
]
matches_cols = [
    np.where(grid[:, c] == "#")[0].tolist() + [height] for c in range(height)
]

print(matches_cols, matches_line)


def toNorth():
    for c in range(len(grid[0])):
        array = grid[:, c]
        matches = matches_cols[c]

        for m in range(len(matches)):
            if m == 0:
                qnt_rocks = array[: matches[m]].tolist().count("O")
                for i in range(matches[m]):
                    grid[i][c] = "O" if i < qnt_rocks else "."
            else:
                qnt_rocks = array[matches[m - 1] : matches[m]].tolist().count("O")
                for i in range(matches[m - 1] + 1, matches[m]):
                    grid[i][c] = "O" if i - (matches[m - 1] + 1) < qnt_rocks else "."


def toWest():
    for r in range(len(grid)):
        array = grid[r]
        matches = matches_line[r]

        for m in range(len(matches)):
            if m == 0:
                qnt_rocks = array[: matches[m]].tolist().count("O")
                for i in range(matches[m]):
                    grid[r][i] = "O" if i < qnt_rocks else "."
            else:
                qnt_rocks = array[matches[m - 1] : matches[m]].tolist().count("O")
                for i in range(matches[m - 1] + 1, matches[m]):
                    grid[r][i] = "O" if i - (matches[m - 1] + 1) < qnt_rocks else "."


def toSouth():
    for c in range(len(grid[0])):
        array = grid[:, c]
        matches = matches_cols[c]

        for m in range(len(matches)):
            if m == 0:
                qnt_rocks = array[: matches[m]].tolist().count(".")
                for i in range(matches[m]):
                    grid[i][c] = "." if i < qnt_rocks else "O"
            else:
                qnt_rocks = array[matches[m - 1] : matches[m]].tolist().count(".")
                for i in range(matches[m - 1] + 1, matches[m]):
                    grid[i][c] = "." if i - (matches[m - 1] + 1) < qnt_rocks else "O"


def toEast():
    for r in range(len(grid)):
        array = grid[r]
        matches = matches_line[r]

        for m in range(len(matches)):
            if m == 0:
                qnt_rocks = array[: matches[m]].tolist().count(".")
                for i in range(matches[m]):
                    grid[r][i] = "." if i < qnt_rocks else "O"
            else:
                qnt_rocks = array[matches[m - 1] : matches[m]].tolist().count(".")
                for i in range(matches[m - 1] + 1, matches[m]):
                    grid[r][i] = "." if i - (matches[m - 1] + 1) < qnt_rocks else "O"


def print_grid():
    for line in grid:
        print(line)
    print()


def calc_total_load():
    total_load = 0

    for i in range(len(grid)):
        line = grid[i]
        qnt_rocks = line.tolist().count("O")
        total_load += qnt_rocks * (height - i)

    return total_load


total_cycles = 1000
for i in range(total_cycles):
    print(f"Progress: {i/total_cycles * 100}% > {i}: {calc_total_load()}")
    toNorth()
    # print_grid()
    toWest()
    # print_grid()
    toSouth()
    # print_grid()
    toEast()
    # print_grid()

print(calc_total_load())
