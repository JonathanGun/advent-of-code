ans = 0
raw_data = []
with open("4.in") as f:
    for line in f:
        raw_data.append(line.strip())

num_cards = [1 for _ in range(len(raw_data))]
for line in raw_data:
    card_metadata, card_data = line.split(":")
    _, card_raw_id = card_metadata.strip().split()
    card_id = int(card_raw_id.strip())
    winning_cards, my_cards = card_data.strip().split("|")
    winning_cards = set(map(int, winning_cards.strip().split()))
    my_cards = set(map(int, my_cards.strip().split()))
    my_winning_cards = my_cards.intersection(winning_cards)

    for i in range(len(my_winning_cards)):
        checkI = card_id + i
        if checkI < len(num_cards):
            num_cards[checkI] += num_cards[card_id - 1]

print(sum(num_cards))
