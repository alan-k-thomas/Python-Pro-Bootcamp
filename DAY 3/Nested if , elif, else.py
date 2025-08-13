condition = "nothing"
another_condition = "just for example"

if condition:
    if another_condition:
        print("Do this")
    else:
        print("Do this")
else:
    print("Do")

#( Roller coaster problem

# input - users height
# if it is greater than 120 cm 
#     one can ride
#         if the person is or under 12yrs old - ticket fare is 5$(if statement)
#         between 12 and 18 = 7$(elif statement)
#         else - 12$(else)
# else 
#     one cannot ride)

height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
if height>=120:
    print("You are eligible to ride")
    if age <12:
        print("Ticket fare is $5")
        #We can use elif conditions as many as we need
    elif age <18: #elif is the 2nd condition, if (if) is not true - it will check elif
        print("Ticket fare is 7$")
    else:
        print("Ticket fare is $12")
else:
    print("Sorry, you are not eleigible to ride")        
