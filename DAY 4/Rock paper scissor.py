# ASCII Art

# Rock
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random

images = [Rock, Paper, Scissor]

# Step 1: Asking user's choice
user_choice = int(input("What do you chose? 0 for Rock, 1 for Paper and 2 for Scissor \n"))

# Step 2: Random computer choice
computer_choice = random.randint(0, 2)

print(f"Your chose : {images[user_choice]}")
print(f"Compter chose : {images[computer_choice]}")

# Step 3: Deciding winner
if user_choice == computer_choice:
    print("Draw")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose")