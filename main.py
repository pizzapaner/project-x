import random

game = True
player_stay = False
dealer_stay = False
player_hand = []
dealer_hand = []
card_history = {
    1: 0, 2: 0, 3: 0, 4: 0,
    5: 0, 6: 0, 7: 0, 8: 0,
    9: 0, 10: 0, 11: 0, 12: 0,
    13: 0
}

num_to_card = {
    1: 'A', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8',
    9: '9', 10: '10', 11: 'J', 12: 'Q',
    13: 'K'
}

card_to_num = {
    'A': 11, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, '10': 10, 'J': 10, 'Q': 10,
    'K': 10
}


def generate_card():
    num = random.randint(1, 13)
    for index in card_history:
        if index == num:
            card_history[index] += 1
    if card_history[num] > 4:
        return generate_card()
    return num


def render(hand):
    hand_render = []
    for card in hand:
        hand_render.append(num_to_card[card])
    return hand_render


def is_bust(hand):
    ace_exists = 0
    for i in range(len(hand)):
        if hand[i] > 10:
            hand[i] = 10
        if hand[i] == 1:
            ace_exists += 1

    if ace_exists:
        hand_min_ace = sum(hand) - 1
        if hand_min_ace + 11 > 21:
            hand_sum = hand_min_ace + 1
        else:
            hand_sum = hand_min_ace + 11
        ace_exists -= 1

        for ace in range(ace_exists):
            hand_sum += 1

    else:
        hand_sum = sum(hand)
    if hand_sum > 21:
        return True
    return False


def hit(hand, card):
    hand.append(card)
    return hand


def dealer_is_safe(hand):
    return sum(hand) <= 16

# Turn 1
player_hand.append(generate_card())
dealer_hand.append(generate_card())

print(render(player_hand))
print(render(dealer_hand))


# Starts game
while game:
    if not player_stay:
        print('PLAYER:')
        user_input = input('Hit or stay?').lower()
        if user_input == 'hit':
            player_hand = hit(player_hand, generate_card())
            print('PLAYER HIT')
        elif user_input == 'stay':
            player_stay = True
            print('PLAYER STAY')
        print(render(player_hand))
    if not dealer_stay:
        print('DEALER:')
        if dealer_is_safe(dealer_hand):
            dealer_hand = hit(dealer_hand, generate_card())
            print('DEALER HIT')
        else:
            dealer_stay = True
            print('DEALER STAY')
        print(render(dealer_hand))

    if is_bust(player_hand) or is_bust(dealer_hand):
        game = False
        print('BUST: GAME OVER\n\n')
    if dealer_stay and player_stay:
        game = False
        print('BOTH STAY: SHOW HANDS\n\n')

#decide_winner(player_hand, dealer_hand)

print('Player:')
print(render(player_hand))
print('\nDealer:')
print(render(dealer_hand))
