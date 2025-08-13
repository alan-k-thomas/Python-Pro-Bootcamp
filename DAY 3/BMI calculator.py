weight = float(input("Enter your weight: "))
height = float(input("Enter your height in meter: "))
#bmi = weight in kg /(height **2)in meter
bmi = weight / (height ** 2)
print(bmi)
# 🚨 Do not modify the values above
# Write your code below 👇

# BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"
if bmi <18.5:
    print("Underweight")
elif bmi <25:
    print("Normal weight")
else:
    print("Overweight")