# The Modulo Operator is something which is often represented by the symbol %.
# It calculates the reminder of a division operation.

print(10%5)
print(10%3)

#Finding a number which is odd or even

#Process breakdown
#Number variable with user input (str to int)
#find modulo operator by dividing with 2
#If the operator is 0 then it is an even number
#If the result is 1 then it is an odd number

Number = int(input("Enter the number you want to check:\n"))
Modulo_operator = Number%2
if Modulo_operator == 0:
    print("It's and even number.")
else:
    print("It's an odd number.")