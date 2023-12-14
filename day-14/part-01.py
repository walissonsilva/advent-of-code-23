import numpy as np

file = open("input.txt")

grid = []

for line in file:
    grid.append(list(line.replace("\n", "")))


grid = np.array(grid)

height = len(grid[0])

total_load = 0

for c in range(len(grid[0])):
    col = grid[:, c]
    matches = np.where(col == "#")[0].tolist()
    matches.append(height)

    for m in range(len(matches)):
        if m == 0:
            qnt_rocks = col[: matches[m]].tolist().count("O")
            load = sum(height - i for i in range(qnt_rocks))
            total_load += load
        else:
            qnt_rocks = col[matches[m - 1] : matches[m]].tolist().count("O")
            load = sum(height - matches[m - 1] - i - 1 for i in range(qnt_rocks))
            total_load += load

        print(qnt_rocks, load)


print(total_load)
