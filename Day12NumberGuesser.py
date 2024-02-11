from random import randint
from Day12NumberGuesser_Art import logo

# Difficulty
EASY_TURNS = 10
HARD_TURNS = 5


# compare guess to randomized number
def compare_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns -1
    elif guess < answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}!")


# set difficulty
def set_difficulty():
    difficulty = input("Chose a difficulty. Easy or Hard?: ").lower()
    if difficulty == "easy":
        return EASY_TURNS
    elif difficulty == "hard":
        return HARD_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guesser")
    print("I'm thinking of a number between 1 and 100: ")
    # randomized integer
    answer = randint(1, 100)
#    print(f"debugger: {answer}")
    turns = set_difficulty()
    # choose a number
    guess = 0
    while guess != answer:
        print(f"You have {turns} to guess the number.")
        guess = int(input("Make a guess: "))
        turns = compare_answer(guess, answer, turns)
        # attempt tracker
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The correct answer was {answer}")
            return


game()
