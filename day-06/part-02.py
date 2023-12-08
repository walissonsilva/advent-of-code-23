
import re

file = open('input.txt')


def multiply_list(lista):
    mult = 1
    for element in lista:
        mult *= element

    return mult


time = []
distance = []

first_line = file.readline()
first_line = first_line.replace(' ', '')
time = [int(d) for d in re.findall('\\d+', first_line)]

second_line = file.readline()
second_line = second_line.replace(' ', '')
distance = [int(d) for d in re.findall('\\d+', second_line)]

longer_distance = multiply_list(distance)
longer_time = multiply_list(time)

print(longer_distance, longer_time)

qtd = 0

for v in range(1, longer_time):
    d = v * (longer_time - v)

    if d > longer_distance:
        qtd += 1

print(qtd)
