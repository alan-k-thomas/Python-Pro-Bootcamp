# This is a mutiline code (''' ''')
print(r''' Welcome to treasure Island!m #use r slashes (because python will stop intepreting with backslashes)
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o\__/o_>     _/ \_   |
             \_________\#/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`''') #ASCII art

print("Your goal is to find the treasure.")

# Story breakdown
# Going to the mysterious island
# Command keys : Left and Right
# ✅ Treasure Island Storyline

# Intro
# You arrive on a mysterious island filled with ancient traps and hidden secrets.
# Your mission is to find the legendary treasure hidden deep inside the island.

# Level 1: The Crossroad
# You walk along a jungle path and reach a crossroad.
# You can go left (towards the beach) or right (towards the dark forest).
# Right → you fall into a trap → Game Over.
# Left → you continue your journey.

# Level 2: The Lake
# You reach a lake with an island in the middle.
# You can either wait for a boat or swim across.
# Swim → you get attacked by crocodiles → Game Over.
# Wait → a boat arrives and takes you safely to the island.

# Level 3: The House of Doors
# On the island, there is a mysterious house with 3 doors – red, yellow, and blue.
# Red door → leads to a room full of fire → Game Over.
# Blue door → leads to a room full of wild beasts → Game Over.
# Yellow door → leads to the treasure room → YOU WIN!

# Ending
# If you find the treasure, you become the greatest explorer of all time!
# If you fail, the island keeps its secret forever.

# user inputs
username = input("Enter your name: ")
print("Hey " + username + "! You arrive on a mysterious island filled with ancient traps and hidden secrets.")
print()
print("Your mission is to find the legendary treasure hidden deep inside the island.")
print()

#task 1

print("Level 1 - Crossroad")
print()
print("You walk along a jungle path and reach a cross road." )
task = input("You can go LEFT (towards the beach) or RIGHT (towards the dark forest): ").upper()
if task == "RIGHT":
    print("You fall into a trap. GAME OVER")
elif task== "LEFT":
    print("You can continue you journey")
    print()
    #task 2

    print("Level 2 - The lake")
    print()
    print("You reach a lake with an island in the middle.")
    task = input("You can either WAIT for a boat or SWIM across: ").upper()
    if task == "SWIM":
        print("You get attacked by crocodiles. GAME OVER")
    elif task== "WAIT":
        print("A boat arrives and takes you safely to the island")
        print()
        #task 3
        
        print("Level 3 - The House of Doors")
        task = input("On the island, there is a 3 mysterious house with 3 doors - YELLOW, RED or BLUE: ").upper()
        if task == "RED":
            print("Leads to a room full of fire. GAME OVER")
        elif task== "BLUE":
            print("Leads to a room full of beasts. GAME OVER")
        elif task== "YELLOW":
            print("leads to the treasure room → YOU WIN!")
            print()
    
# ending
            print("You became the greatest explorer of all time!")





