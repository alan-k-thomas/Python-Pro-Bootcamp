# Our goal is to build a Hangman game.

# TO DO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TO DO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TO DO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.


# To do-1
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

# To do-2
# Create a place_holder with the same number of blanks as the chosen_word
guess = input("Guess a letter: ").lower()

# To do-3
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")