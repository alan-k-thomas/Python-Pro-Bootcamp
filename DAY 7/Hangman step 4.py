stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


 
import random

# Todo 1 - create a variable called lives to keep track the number of lives the user has left. 
# Set lives equal to 6
lives = 6

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Start with underscores as placeholders
display = ["_"] * len(chosen_word)

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Update display with the guessed letter if it's in the word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(" ".join(display))  # shows progress neatly with spaces


# Todo 2- If guess is not a letter in chosen_word, then reduce 'lives' by 1
# If the lives goes down to zero, then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")
          

# Check if the player has guessed the whole word
    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])
