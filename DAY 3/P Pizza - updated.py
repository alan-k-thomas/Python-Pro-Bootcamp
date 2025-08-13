# Greeting
print("🍕Welcome to Python pizza deliveries!🍕")

# Inputs
size = input("Which size pizza do you want? Small(S), Medium(M) or Large(L): ")
add_pepperoni = input("Do you want to add pepperoni? Type Yes(Y) or No(N): ")
extra_cheese = input("Do you want extra cheese? Yes(Y) or No(N): ")

# Base bill
bill = 0

# step 1 = Add base pizza price
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("❌Invalid size, please type correct informations")
    exit() # Stop the programme

# step 2 = Add pepperoni
if add_pepperoni == "Y":
    if size == "S": # Small
        bill += 2
    else:           # Medium, Large
        bill += 3

#Step 3 = Extra cheese
if extra_cheese == "Y":
    bill += 1

#Step 4 = Final price
print(f"Your final price is {bill}$")