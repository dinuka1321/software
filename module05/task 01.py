import random

dice_count = int(input("How many dice do you want to roll? "))

total = 0
for i in range(dice_count):
    roll = random.randint(1, 6)
    total += roll

print("The total sum of the dice rolls is:", total)