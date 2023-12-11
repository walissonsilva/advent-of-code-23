import numpy as np

file = open('example.txt')

mtx = []

for line in file:
    line_list = [symbol for symbol in line if symbol != '\n']

    if '#' not in line_list:
        mtx.append(line_list)

    mtx.append(line_list)

mtx = np.array(mtx)

for line in mtx:
    print(line)

col_index = 0

while col_index < len(mtx[0]):
    column = mtx[:, col_index]
    if '#' not in mtx[:, col_index]:
        print(col_index)
        mtx = np.insert(mtx, col_index, column, axis=1)

        col_index += 1

    col_index += 1


class Graph:
    def __init__(self, grid):
        self.grid = grid

    @staticmethod
    def isValid(x, y, visited):
        if x >= 0 and x < visited.shape[0] and y >= 0 and y < visited.shape[1] and visited[x, y] == -1:
            return True
        return False

    def BFS(self, source, destination):
        queue = []
        visited = np.full_like(self.grid, -1, dtype=int)

        queue.append([(source[0], source[1]), 0])
        visited[source[0], source[1]] = 0

        shortest_path = -1

        while len(queue) != 0:
            pos, steps = queue.pop(0)
            x, y = pos
            print(x, y)

            if Graph.isValid(x - 1, y, visited):
                queue.append([(x - 1, y), steps + 1])
                visited[x - 1, y] = steps + 1
            if Graph.isValid(x, y - 1, visited):
                queue.append([(x, y - 1), steps + 1])
                visited[x, y - 1] = steps + 1
            if Graph.isValid(x + 1, y, visited):
                queue.append([(x + 1, y), steps + 1])
                visited[x + 1, y] = steps + 1
            if Graph.isValid(x, y + 1, visited):
                queue.append([(x, y + 1), steps + 1])
                visited[x, y + 1] = steps + 1

            if (x, y) == destination:
                shortest_path = steps

        return visited


graph = Graph(mtx)

where_galaxies = np.where(mtx == '#')
galaxies_position = list(zip(where_galaxies[0], where_galaxies[1]))

sum = 0
visited_left = graph.BFS((0, 0), (mtx.shape[0] - 1, mtx.shape[1] - 1))
visited_right = graph.BFS(
    (0, mtx.shape[1] - 1), (mtx.shape[0] - 1, 0))

for source_index in range(len(galaxies_position)):
    for destination_index in range(len(galaxies_position)):
        if destination_index > source_index:
            source, destination = galaxies_position[source_index], galaxies_position[destination_index]
            if source[0] < destination[0]:
                print(visited_left[destination[0], destination[1]])
                print(visited_left[source[0], source[1]])
                result = abs(visited_left[destination[0], destination[1]] -
                             visited_left[source[0], source[1]])
            if source[0] < destination[0]:
                print(visited_right[destination[0], destination[1]])
                result = abs(visited_right[destination[0], destination[1]] -
                             visited_right[source[0], source[1]])
            # print(result)
            sum += result
            print(source_index + 1, destination_index + 1, result)

print(sum)

for line in visited_right:
    print(line)
for line in visited_left:
    print(line)
