#if multiple condtions are needed to be executed
#We use multiple if statements

#( Roller coaster problem

# input - users height
# if it is greater than 120 cm 
#     one can ride
#         if the person is or under 12yrs old - ticket fare is 5$(if statement)
#           bill = 5$
#         between 12 and 18 = 7$(elif statement)
#           bill = 7$
#         else - 12$(else)
#           bill = 12$
#      ask they want photo taken? If yes it will cost 3$
#       Total bill will be bill =+ 3 (bill = bill + 3)
# else 
#     one cannot ride)
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
if height>=120:
    print("You are eligible to ride")
    if age <12:
        print("Ticket fare is $5")
        bill = 5
    elif age <18: 
        print("Ticket fare is 7$")
        bill = 7
    else:
        print("Ticket fare is $12")
        bill = 12

    photo = input("Do you want to take your photos?Type y for yes and n for no:\n")
    if photo == "y":
        # add 3$ to the bill
        bill += 3 #(bill = bill + 3)
        print(f"Your final bill is {bill}$")
    else:
        print("Your total fare is same as the ticket fare")
else:
    print("Sorry, you are not eleigible to ride")   
