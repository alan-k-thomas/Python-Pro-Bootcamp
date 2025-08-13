# List Data structure


# A simple collection of ordered items using a Python list. e.g.
fruits = ["Apple", "Cherry", "Orange"]



# Accessing Items in Lists
# You can provide the name of the list then a square bracket and then the item index that you want. e.g.

fruits[0] # will give you "Apple".

# Remember that everything computer related, the first number we count with is 0 and never 1. 0, 1, 2, 3 instead of 1, 2, 3 4.

# Negative Indices
# You can access items in the list counting from the end of the list by using negative whole numbers. e.g.

fruits = ["Cherry", "Apple", "Pear"]
fruits[-1] #this will be "Pear"

# Modifying Items
# You can use the same syntax to get hold of items in a List to modify it. e.g.

fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange"
# fruits will now become ["Orange", "Apple", "Pear"]

# Adding Items
# You can add items to the end of a List using the append() function. e.g.

fruits = ["Cherry", "Apple", "Pear"]
fruits.append("Orange")
# fruits will now become ["Cherry", "Apple", "Pear", "Orange"]