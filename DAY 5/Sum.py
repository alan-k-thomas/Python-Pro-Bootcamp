# Sum

# Python has lots of built-in functions to help us work with numbers.
# One of them helps us to calculate the sum (the total). e.g.

student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores)
print(total_score)


# Or we can find the sum using the manual way

# Step 1: Creating a variable to store the sum values

sum = 0 #inital value will be zero
for score in student_scores:
    sum += score # each time the score is adding with the previous value and storing in sum variable.
print(sum)


