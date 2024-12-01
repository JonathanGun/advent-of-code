from collections import Counter
from functools import reduce

def to_card_value(ch):
    if '0' <= ch <= '9':
        return int(ch)
    ranks = ['T', 'J', 'Q', 'K', 'A']
    return ranks.index(ch) + 10

def power(hand):
    # 5, 41, 32, 311, 221, 2111, 11111
    return sorted(Counter(hand).values(), reverse=True)

n = int(input())

all_cards = []
for _ in range(n):
    card, bid = input().split()
    card_values = list(map(to_card_value, card))
    # sort by: power, card_values, bid. sum(bid * index) is the answer
    all_cards.append((power(card_values), card_values, int(bid)))
all_cards.sort()
for card in all_cards:
    print(card)
print(sum([(i + 1) * card[2] for i, card in enumerate(all_cards)]))
