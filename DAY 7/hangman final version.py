import random

# Todo 1 - Update the word list to use the word_list from hangman_words.py
from hangman_words import word_list
from hangman_ascii import stages, logo
lives = 6

# Todo 3 - Import the logo from hangman_ascii and print it at the start of the game.
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

display = ["_"] * len(chosen_word)

game_over = False

while not game_over:
    # Todo 4 - Update the code below to tell the user how many lives they have left.
    print(f"************************{lives}/6 LIVES LEFT**************************")
    guess = input("Guess a letter: ").lower()

    # Todo 4 - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}")
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(" ".join(display))  

    # Todo 5 - If the guessed letter is not in the word list, print you have guessed a wrong letter.

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.")
        if lives == 0:
            game_over = True
    # Todo 7 - Update the print statement and let the user know the correct word.
            print(f"*************************The correct word was {chosen_word}! You lose***************************")

          


    if "_" not in display:
        game_over = True
        print("You win!")

#Todo - 2: Update the code below to use the stages list from hangman_ascii.py
    print(stages[lives])
