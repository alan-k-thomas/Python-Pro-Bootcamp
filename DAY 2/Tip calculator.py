print("Welcome to tip calculator!")
Bill = float(input("Enter the total bill amount please: $ "))

Tip_percentage = float(input("How much percentage of tip is to be added? (10, 12, 15): "))
Tip = (Tip_percentage/100 * Bill) 
Total_amount = (Bill + Tip)

Split = float(input("Number of persons to split the amount: "))

each_one_amount = round(Total_amount/Split, 2)
print(f"Your total amount will be {Total_amount} and each one should pay about {each_one_amount}")