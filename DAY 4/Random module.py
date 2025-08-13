# The random module in Python is a built-in module that provides functions 
# for generating pseudo-random numbers and performing random operations. 

# It is widely used in various applications, including simulations, games, 
# data shuffling, and randomized algorithms. 

#Firstly we have to import random module to our code
import random

# Returns a random integer between a and b (inclusive)
print(random.randint(1, 10)) 

# Returns a random float between 0.0 and 1.0(random)
print(random.random())
print(random.random()* 10) # if will give an answer multiplied by 10

# Returns a random float between a and b(uniform)
print(random.uniform(1, 5))

# Picks one random item from a tuple or list.(Sequence)
colors = ["Red", "White", "Black"]
print(random.choice(colors))

# Shuffles a list in a random order.
deck = [1, 2, 3, 4, 5, 6]
random.shuffle(deck)
print(deck)

# Returns k random unique items from a list (population, k)
numbers = [1, 2, 3, 4, 5, 6]
print(random.sample(numbers, 3))

# Seed (Returns the same reproducible random results)
random.seed(5) # Fix the randomness
print(random.randint(1, 10))


# Quick Summary

# randint(a, b) → random integer in range
# random() → random float from 0 to 1
# uniform(a, b) → random float in range
# choice(list) → random item from list
# shuffle(list) → randomly reorder a list
# sample(list, k) → randomly pick k items
# seed(n) → make random results predictable