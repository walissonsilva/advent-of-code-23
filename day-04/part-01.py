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


scores = 0

for line in file:
    input = line.split(': ')[1]
    input = input.replace('\n', '')
    winning, mine = input.split(' | ')

    winning = [card for card in winning.split(' ') if card != '']
    mine = [card for card in mine.split(' ') if card != '']

    matches = get_matches(winning, mine)

    scores += get_score(len(matches))


print(scores)
