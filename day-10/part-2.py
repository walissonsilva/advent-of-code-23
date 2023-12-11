file = open('example5.txt')


class Graph:
    def __init__(self):
        self.adj = {}

    @staticmethod
    def get_visited():
        visited = []
        for i in range(rows):
            for j in range(cols):
                if j == 0:
                    visited.append([(False, 0)])
                else:
                    visited[i].append((False, 0))

        return visited

    def add_connection(self, a, b):
        try:
            if b not in self.adj[a]:
                self.adj[a].append(b)
        except Exception as e:
            self.adj[a] = [b]
        try:
            if a not in self.adj[b]:
                self.adj[b].append(a)
        except Exception as e:
            self.adj[b] = [a]

    def DFS(self, v, visited, depth=0):
        print(v)
        visited[v[0]][v[1]] = (True, depth)

        for i in self.adj[v]:
            print(i)
            if visited[i[0]][i[1]] == (False, 0):
                self.DFS(i, visited, depth + 1)

    def BFS(self, v):
        # Mark all the vertices as not visited
        visited = []
        for i in range(rows):
            for j in range(cols):
                if j == 0:
                    visited.append([(False, 0)])
                else:
                    visited[i].append((False, 0))
        # visited = [False] * (rows * cols + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append((v, 0))
        visited[v[0]][v[1]] = (True, 0)

        max_depth = 0
        while queue:
            # Dequeue a vertex from
            # queue and print it
            s, depth = queue.pop(0)
            # print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s.
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.adj[s]:
                if visited[i[0]][i[1]] == (False, 0):
                    queue.append((i, depth + 1))
                    visited[i[0]][i[1]] = (True, depth + 1)

            # print_visited(visited)
            # input()

            if max_depth < depth:
                max_depth = depth

            print_visited(visited)
            input()

        print_visited(visited)

        return 0


def print_visited(visited):
    inside = 0
    for i in range(rows):
        is_in = False
        line = ''
        for j in range(cols):
            if j > 0:
                if visited[i][j][1] != 0 and visited[i][j-1][1] == 0 and mtx[i][j-1] != 'S':
                    is_in = not is_in
                # if visited[i][j][1] == 0 and mtx[i][j] != 'S' and visited[i][j-1][1] != 0:
                #     is_in = not is_in

            if visited[i][j][1] == 0 and mtx[i][j] != 'S' and not is_in:
                # line += 'O'.rjust(4)
                line += '.'.rjust(4)
            elif visited[i][j][1] == 0 and mtx[i][j] != 'S' and is_in:
                # line += 'I'.rjust(4)
                line += '.'.rjust(4)
                inside += 1
            else:
                line += str(visited[i][j][1]).rjust(4)  # mtx[i][j]
                # line += str(mtx[i][j]).rjust(2)

        print(line)


graph = Graph()

idx = 0
x = 0
y = 0

mtx = []

for line in file:
    line_list = [el for el in line if el != '\n']
    mtx.append(line_list)

rows = len(mtx)
cols = len(mtx[0])

start_pos = (0, 0)

for i in range(rows):
    for j in range(cols):
        el = mtx[i][j]
        if el == '|' and i - 1 >= 0 and i + 1 < rows:
            if mtx[i - 1][j] != '.' and mtx[i - 1][j] in ['S', 'F', '|', '7']:
                graph.add_connection((i - 1, j), (i, j))
            if mtx[i + 1][j] != '.' and mtx[i + 1][j] in ['S', '|', 'J', 'L']:
                graph.add_connection((i + 1, j), (i, j))
        elif el == '-' and j - 1 >= 0 and j + 1 < cols:
            if mtx[i][j + 1] != '.' and mtx[i][j + 1] in ['-', 'S', '7', 'J']:
                graph.add_connection((i, j + 1), (i, j))
            if mtx[i][j - 1] != '.' and mtx[i][j - 1] in ['-', 'S', 'F', 'L']:
                graph.add_connection((i, j - 1), (i, j))
        elif el == '7' and j - 1 >= 0 and i + 1 < rows:
            if mtx[i][j - 1] != '.' and mtx[i][j - 1] in ['-', 'S', 'F', 'L']:
                graph.add_connection((i, j - 1), (i, j))
            if mtx[i + 1][j] != '.' and mtx[i + 1][j] in ['S', '|', 'J', 'L']:
                graph.add_connection((i + 1, j), (i, j))
        elif el == 'J' and j - 1 >= 0 and i - 1 >= 0:
            if mtx[i][j - 1] != '.' and mtx[i][j - 1] in ['-', 'S', 'F', 'L']:
                graph.add_connection((i, j - 1), (i, j))
            if mtx[i - 1][j] != '.' and mtx[i - 1][j] in ['S', 'F', '|', '7']:
                graph.add_connection((i - 1, j), (i, j))
        elif el == 'F' and j + 1 < cols and i + 1 < rows:
            if mtx[i][j + 1] != '.' and mtx[i][j + 1] in ['-', 'S', '7', 'J']:
                graph.add_connection((i, j + 1), (i, j))
            if mtx[i + 1][j] != '.' and mtx[i + 1][j] in ['S', '|', 'J', 'L']:
                graph.add_connection((i + 1, j), (i, j))
        elif el == 'L' and j + 1 < cols and i - 1 >= 0:
            if mtx[i][j + 1] != '.' and mtx[i][j + 1] in ['-', 'S', '7', 'J']:
                graph.add_connection((i, j + 1), (i, j))
            if mtx[i - 1][j] != '.' and mtx[i - 1][j] in ['S', '|', 'F', '7']:
                graph.add_connection((i - 1, j), (i, j))

        if el == 'S':
            start_pos = (i, j)

visited = Graph.get_visited()
print(graph.DFS(start_pos, visited))
print_visited(visited)
