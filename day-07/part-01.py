file = open('input.txt')

# Five of kind: 0
# Four of kind: 1
# Full house: 2
# Three of kind: 3
# Two pair: 4
# One pair: 5
# High card: 6

card_value_mapping = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13,
}


def get_cards_config(cards):
    cards_set = set(cards)
    number_of_each = {}
    strength = 0

    for i in range(len(cards)):
        card_value = card_value_mapping[cards[i]]
        card_relevancy = 5 - i

        strength += card_value * 13 ** card_relevancy

        try:
            number_of_each[card_value] += 1
        except Exception as e:
            number_of_each[card_value] = 1

    number_of_each = sorted(list(number_of_each.values()))

    if len(cards_set) == 1:
        return 7, strength

    if len(cards_set) == 2:
        a, b = number_of_each
        if a == 1 and b == 4:
            return 6, strength

        return 5, strength
    if len(cards_set) == 3:
        a, b, c = number_of_each
        if a == 1 and b == 1 and c == 3:
            return 4, strength

        return 3, strength

    if len(cards_set) == 4:
        return 2, strength

    return 1, strength


hands = []

for line in file:
    cards, rank = line.replace('\n', '').split(' ')

    cards_config = get_cards_config(cards)

    hands.append({'cards': cards, 'bid': int(rank), 'config': cards_config})


hands = sorted(hands, key=lambda d: (
    d['config'][0], d['config'][1]), reverse=False)

result = 0

for i in range(len(hands)):
    print(hands[i]['config'], hands[i]['bid'], i + 1)
    result += hands[i]['bid'] * (i + 1)


print(result)
