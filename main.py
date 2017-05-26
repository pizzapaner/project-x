import random

player_hand = []
dealer_hand = []
card_history = {
    1: 0, 2: 0, 3: 0, 4: 0,
    5: 0, 6: 0, 7: 0, 8: 0,
    9: 0, 10: 0, 11: 0, 12: 0,
    13: 0
}

num_to_card = {
    1: 'A', 2: '2'
}

card_to_num = {

}

def generate_card():
    num = random.randint(1, 13)
    for index in card_history:
        if index == num:
            card_history[index] += 1
    if card_history[num] > 4:
        return generate_card()
    return num

# Turn 1
player_hand.append(generate_card())
dealer_hand.append(generate_card())

print(player_hand[0])
print(dealer_hand)

# played_cards = []
# while(len(played_cards) != 52):
#     card = generate_card()
#     played_cards.append(card)
#     print(card)
#     print('played cards: ' + str(len(played_cards)))
# print(card_history)

