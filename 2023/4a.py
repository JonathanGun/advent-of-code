ans = 0
with open("4.in") as f:
    for line in f:
        card_metadata, card_data = line.split(":")
        _, card_raw_id = card_metadata.strip().split()
        card_id = int(card_raw_id.strip())
        winning_cards, my_cards = card_data.strip().split("|")
        winning_cards = set(map(int, winning_cards.strip().split()))
        my_cards = set(map(int, my_cards.strip().split()))
        my_winning_cards = my_cards.intersection(winning_cards)
        points = 0
        if my_winning_cards:
            points += 2**(len(my_winning_cards) - 1)
        ans += points
print(ans)
