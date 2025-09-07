import random

def rolldice(sides):
    return random.randint(1, sides)

def main():
    sides = int(input("Enter number of sides on the dice: "))
    roll = 0
    while roll != sides:
        roll = rolldice(sides)
        print("Rolled:", roll)

main()