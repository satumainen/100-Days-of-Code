
import random
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Returns sum of card values"""
    if sum(cards) == 21 and len(cards) == 2: #a blackjack hand
        return 0 #a blackjack score was found
    if 11 in cards and sum(cards) > 21: #if score is over 21, 11 is counted as 1
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "You lose, opponent has a Blackjack!"
    elif u_score == 0:
        return "You win with a Blackjack!"
    elif u_score > 21:
        return "You went over, you lose!"
    elif c_score > 21:
        return "Your opponent went over, you win!"
    elif u_score > c_score:
        return "You won!"
    else:
        return "You lost"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        """Deals two cards to each player"""
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards {user_cards}, current score {user_score}")
        print(f"Computers first card {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to quit ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computers first card {computer_cards[0]}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? (y/n) ") == "y":
    play_game()