# PAUSE 1 - Max
# There are also a built-in Python methods called max() and min(), 
# which allow you to pass in a List of numbers, 
# and it will give you the highest number or the lowest number.

# Your job is to figure out how the Python programmers might have built this 
# functionality using loops and conditionals.

# COMPLETE THIS CHALLENGE WITHOUT USING max()
# You are given a list of exam scores, and you have to print out the highest score 
# from the List. You will need to use what you have learnt about Lists, 
# For Loops and Conditionals to print out the highest score in the list of student_scores.
# For example, if the scores were:

# 8 65 89 86 55 91 64 89
# Your code should print

# 91

scores = [8, 65, 89, 86, 55, 91, 64, 89]

# step 1: Start by assuming the first number is the highest
highest_score = scores[0]

# step 2: Finding highest score using loop
for score in scores:
    if score > highest_score:
        highest_score = scores # = is assign function, not equal to function

# step 3: Printing the highest score
print(f"The highest number is :{highest_score}")


# the other built in function is using max

max_score = max(scores)
print(max_score)

