from art import logo, vs
from game_data import data
import random

score = 0
game_should_continue = True
account_b = random.choice(data)

def format_data(account):
    """Takes the account data and returns it in a printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, {account_descr}, from {account_country}")

def check_answer(a_follower_count, b_follower_count, guess):
    """Checks if the guess is correct and returns whether the guess was true or not"""
    if a_follower_count > b_follower_count:
        return guess == "a"
    elif a_follower_count < b_follower_count:
        return guess == "b"

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(logo)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(a_follower_count, b_follower_count, guess)

    if is_correct:
        score += 1
        print(f"You got it! Current score is: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
