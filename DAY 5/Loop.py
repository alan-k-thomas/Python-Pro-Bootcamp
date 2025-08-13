# Loops allow us to tell the computer to repeat actions without having to write repeated code. 
# If we wanted the computer to print out 1 through to 100, 
# it would be very painful to type a print statement for every number, 
# or even just typing out all the numbers 1 through to 100.
# Loops allow us to create a rule and the computer can follow it to do a repeated action.

# Syntax

# for <variable name of each item> in <a List>:
#     <do something>
#     <do something else> e.g.

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits: # fruit is the variable name which we give for each item. 
    print(fruit)     # by printing fruit, it will print all values stored inside the list fruits.
    print(fruit + " pie")

        