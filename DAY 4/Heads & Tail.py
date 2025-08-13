# Head or tail toss

import random
toss = ["Head", "Tail"]
print(random.choice(toss))


# or (by using if conditions)

number = random.randint(0, 1)
if number == 0:
    print("Head")
else:
    print("Tail")