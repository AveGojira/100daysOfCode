import random

from Day7Hangman_WordList import word_list
from Day7Hangman_Art import logo, stages

chosen_word = random.choice(word_list)

lives = 6
display_length = len(chosen_word)

print(logo)

display = []
for _ in range(display_length):
    display += "_"
print(''.join(display))

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(display_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter.upper()
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(''.join(display))

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
