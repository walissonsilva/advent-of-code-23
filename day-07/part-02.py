file = open('input.txt')

# Five of kind: 0
# Four of kind: 1
# Full house: 2
# Three of kind: 3
# Two pair: 4
# One pair: 5
# High card: 6

card_value_mapping = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 11,
    'K': 12,
    'A': 13,
}


def get_cards_config(cards):
    most_frequent_card = 'J'
    most_frequent_card_frequency = 0

    number_of_each = {}

    strength = 0

    for i in range(len(cards)):
        card = cards[i]

        if card == 'J':
            continue

        try:
            number_of_each[card] += 1
        except Exception as e:
            number_of_each[card] = 1

    print(number_of_each)
    for card, frequency in number_of_each.items():
        if most_frequent_card_frequency <= frequency:
            most_frequent_card_frequency = frequency
            most_frequent_card = card

    print(most_frequent_card)

    cards_replaced = cards.replace('J', most_frequent_card)
    cards_set = set(cards_replaced)
    number_of_each = {}

    for i in range(len(cards)):
        card = cards_replaced[i]
        card_value = card_value_mapping[cards[i]]
        card_relevancy = 5 - i

        strength += card_value * 13 ** card_relevancy

        try:
            number_of_each[card] += 1
        except Exception as e:
            number_of_each[card] = 1

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
    # print(hands[i]['cards'], hands[i]['config'], hands[i]['bid'], i + 1)
    result += hands[i]['bid'] * (i + 1)


print(result)
