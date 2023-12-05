file = open('input.txt')


def get_matches(winning, mine):
    matches = []

    for card in mine:
        try:
            winning.index(card)
            matches.append(card)
        except:
            pass

    return matches


def get_score(number_of_matches):
    if number_of_matches == 0:
        return 0

    return 2**(number_of_matches - 1)


card = 1
number_of_processing = 0

processing = {}

for line in file:
    try:
        processing[card] += 1
    except:
        processing[card] = 1

    input = line.split(': ')[1]
    input = input.replace('\n', '')
    winning, mine = input.split(' | ')

    winning = [card for card in winning.split(' ') if card != '']
    mine = [card for card in mine.split(' ') if card != '']

    matches = get_matches(winning, mine)

    number_of_matches = len(matches)

    for i in range(1, number_of_matches + 1):
        try:
            processing[card + i] += processing[card]
        except:
            processing[card + i] = processing[card]

    print(processing, number_of_matches, matches)

    card += 1

print(sum([int(value) for [key, value] in processing.items() if key < card]))
