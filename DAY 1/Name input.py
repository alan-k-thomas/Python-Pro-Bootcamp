name = input("Enter your name.")
print("Hello," + name + "!" )

# Since variable name here is an integer value, to concatenate the variables : We use 'f'
# In this way we can find the number of characters in a name.
print(f"Your name has {len(name)} characters.")

#OR

print(f"Your name has {len(input("Enter your name."))} characters.")


