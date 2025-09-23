import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

place_holder = " "
world_length = len(chosen_word)
for position in range(world_length):
    place_holder += "_"
print(place_holder)

# TO DO-1
# Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word.
# At that point display has no more blanks ("_"). Then you can tell the user they've won.

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = " "


# TO DO-2
# Update the for loop so that previous guesses are added to the display String.
# At the moment, when the user makes a new guess, the previous guess gets replaced by a "_". 
# We need to fix that by updating the for loop.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")