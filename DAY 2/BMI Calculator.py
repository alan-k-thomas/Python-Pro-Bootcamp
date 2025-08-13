height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.


bmi = (weight / height ** 2)

#Actual value
print(bmi) #float

#This is called flooring
print(int(bmi)) #integer

#round function - traditional mathematical rounding (converts to the nearest possible whole number)
print(round(bmi))

#rounding upto 2 places 
print(round(bmi, 2)) #add coma and put the number of places which wanted to be rounded.