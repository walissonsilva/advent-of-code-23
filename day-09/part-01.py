file = open('input.txt')

result = 0
nexts = []

for line in file:
    oasis = []

    base_values = [int(value) for value in line.replace('\n', '').split(' ')]

    oasis.append(base_values.copy())

    while len(list(filter(lambda v: v != 0, oasis[-1]))):
        new_line = []
        for i in range(len(oasis[-1]) - 1, 0, -1):
            current_line = oasis[-1]
            new_line.insert(0, current_line[i] - current_line[i - 1])

        oasis.append(new_line.copy())

    oasis.reverse()

    oasis[0].append(0)

    for i in range(1, len(oasis)):
        oasis[i].append(oasis[i - 1][-1] + oasis[i][-1])

    next = oasis[-1][-1]
    nexts.append(next)
    result += next

print(result)
print(sum(nexts))
