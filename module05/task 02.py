numbers = []

user_input = input("Enter a number (or press Enter to quit): ")

while user_input != "":
    numbers.append(int(user_input))
    user_input = input("Enter a number (or press Enter to quit): ")

numbers.sort(reverse=True)

print("The five greatest numbers are:")
for num in numbers[:5]:
    print(num)