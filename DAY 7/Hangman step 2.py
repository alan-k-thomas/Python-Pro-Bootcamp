# TO DO-1
# Create an empty String called placeholder.
# For each letter in the chosen_word, add a _ to placeholder.
# So if the chosen_word was "apple", placeholder should be _ _ _ _ _ with 5 "_" representing each letter to guess.

# TO DO-2
# Create an empty string called "display".
# Loop through each letter in the chosen_word
# If the letter at that position matches guess then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be _ p p _ _.
# Print display and you should see the guessed letter in the correct position.
# But every letter that is not a match is represented with a "_".

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

place_holder = ""
word_length = len(chosen_word)
for position in range(word_length):
    place_holder += "_"
print(place_holder)

# or

place_holder = "-" * len(chosen_word)
print(place_holder)

# Use a while loop to create a guess input for user
guess = input("Guess a letter: ").lower()

display = ""

# Change the for loop so that you keep the previous correct letters in display.
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)