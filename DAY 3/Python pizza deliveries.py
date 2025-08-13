# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1

print("Welcome to Python pizza deliveries!")
pizza_size = input("Which size pizza do you want? Small, Medium or Large: ")
pepperoni = input("do you want to add pepperoni? Type Yes or No: ")
cheese = input("Do you want extra cheese? Yes or No: ")
if pizza_size == "Small":
    if pepperoni == "Yes":
        if cheese == "Yes":
            print("Your bill amount is 18$")
        else:
            print("Your bill amount is 17$")
    if pepperoni == "No":
            print("Your bill amount is 15$")
elif pizza_size == "Medium":
    if pepperoni == "Yes":
        if cheese == "Yes":
            print("Your bill amount is 24$")
        else:
            print("Your bill amount is 23$")
    if pepperoni == "No":
        print("Your bill amount is 20$")
else:
    if pepperoni == "Yes":
        if cheese == "Yes":
            print("Your bill amount is 29$")
        else:
            print("Your bill amount is 28$")
    if pepperoni == "No":
        print("Your bill amount is 25$")