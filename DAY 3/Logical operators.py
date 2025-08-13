# Logical Operators
# And, or , not

# We can combine different conditions using logical operators.

A = 1
B = 2
C = 3
D = 4
E = 5

A and B # Both condtions need to be true
C or D # Only one condition need to be true
not E # The condition must be false

# Again working on the roller coaster problem
# Object : Adding age specific( 45 to 55 (both inclusive) can ride for free )


height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))

if height>=120:
    print("You are eligible to ride.")
    if age <12:
        print("Ticket fare is $5")

    elif age <18: #elif is the 2nd condition, if (if) is not true - it will check elif
        #We can use elif conditions as many as we need
        print("Ticket fare is 7$")
        #both condtions need to be true.

    elif age >=45 and age <=55: #add the variable "age" again after and. 
        # OR
        # 45 <= age <=55
        print("You can ride for free.")


    else:
        print("Ticket fare is $12")

else:
    print("Sorry, you are not eleigible to ride.") 