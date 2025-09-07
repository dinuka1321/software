import random

def rolldice():
    return random.randint(1, 6)

def main():
    roll = 0
    while roll != 6:
        roll = rolldice()
        print("Rolled:", roll)

main()
