# TO DO-1
# Create an empty String called placeholder.
# For each letter in the chosen_word, add a _ to placeholder.
# So if the chosen_word was "apple", placeholder should be _ _ _ _ _ with 5 "_" representing each letter to guess.

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