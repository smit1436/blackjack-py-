import random

#########################################################################

def deal_card():
    """"returns a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]
    random_card = random.choice(cards)
    return random_card

#########################################################################

def calculate_score(cards):
    """take a list of cards and return the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0            ##### here 0 represents blackjack

    ### if score is > 21 and cards contain ace(11) then convert that ace into ace(1) so user or computer dont lose

    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#############################################################################

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "its draw"
    elif computer_score == 0 :
        return "lose , opponent has blackjack"
    elif user_score == 0:
        return "win with a blackjack"
    elif user_score > 21 :
        return "lose, you went over"
    elif computer_score >21:
        return "opponent went over , you won"
    elif user_score > computer_score:
        return "you won"
    elif user_score < computer_score:
        return "you lose"

###############################################################################

def play_game():
    user_card = []
    computer_card = []

    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"user card is {user_card} and user_score: {user_score}")
        print(f"computer card is {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_continue = input("'y' to deal another card or 'n' to pass:")
            if user_should_continue == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_card.append(deal_card())
            computer_score = calculate_score(computer_card)

    print(f" your card : {user_card} score : {user_score}")
    print(f" computer card: {computer_card} score: {computer_score}")

    print(compare(user_score,computer_score))

while input("to start thr game hit 'y':") == "y" :
    
    play_game()