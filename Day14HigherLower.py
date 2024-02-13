from Day14HigherLower_Art import logo, vs
from Day14HigherLower_Data import data
import random
from os import system


def format_data(choice):
    """Formats the choice data into a readable output."""
    choice_name = choice["name"]
    choice_description = choice["description"]
    choice_country = choice["country"]
    return f"{choice_name}, a {choice_description}, from {choice_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the users guess and the follower counts from A and B and returns if they got it correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def clear():
    _ = system('cls')


# Initialize the score
score = 0

continue_game = True
# randomize the "B" choice
choice_b = random.choice(data)
print(logo)
# Loops game while winning
while continue_game:

    choice_a = choice_b
    choice_b = random.choice(data)

    if choice_a == choice_b:
        choice_b = random.choice(data)

    print(f"Compare A: {format_data(choice_a)}.")
    print(vs)
    print(f"Against B: {format_data(choice_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = choice_a["follower_count"]
    b_follower_count = choice_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # clears the screen to keep UX clean.
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"That is correct! Current score is {score}.")
    else:
        print(f"Sorry that is wrong. Final score is {score}.")
        input("Press [ENTER] to exit.")
        continue_game = False
