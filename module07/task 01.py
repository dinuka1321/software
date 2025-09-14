
seasons = ("spring","summer","autumn","winter")

def main(num):
    if 1<=num<=2 or num == 12:
        month = 0
    elif 3<=num<=6:
        month = 1
    elif 7<=num<=9:
        month = 2
    else:
        month = 3
    return month
num = int(input("enter month : " ))
month = main(num)
print(f"season is {seasons[month]}")