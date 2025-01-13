from random import randint
from art import logo

print(logo)

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose the difficulty. Type 'easy' or 'hard': ")
    number_of_guesses = -1
    number = randint(1, 100)
    attempt = 1
    if level == "easy":
        number_of_guesses = 10
    elif level == "hard":
        number_of_guesses = 5
    while attempt <= number_of_guesses:
        print(f"This is attempt number {attempt}/{number_of_guesses}.")
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == number:
            print(f"You guessed the correct number {guess}.")
            break
        elif guess > number:
            print(f"Too high, you guessed {guess}.")
        else:
            print(f"Too low, you guessed {guess}.")
        attempt += 1
    print(f"Thank you for playing! The correct number was {number}")

number_guessing_game()