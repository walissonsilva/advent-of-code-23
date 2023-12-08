import re

file = open('input.txt')

time = []
distance = []

first_line = file.readline()
time = [int(d) for d in re.findall('\\d+', first_line)]

second_line = file.readline()
distance = [int(d) for d in re.findall('\\d+', second_line)]

total = 1

for i in range(len(time)):
    qtd = 0

    for v in range(1, time[i]):
        d = v * (time[i] - v)

        if d > distance[i]:
            qtd += 1

    total *= qtd

print(total)
