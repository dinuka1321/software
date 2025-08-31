numbers = []
value = input("Enter a number (or press Enter to quit): ")

while value !=  "":
    numbers.append(float(value))
    value = input("Enter a number (or press Enter to quit): ")
    minimum = min(numbers)
    maximum = max(numbers)
if numbers:
    print(f"Smallest number is {minimum} and Largest number is {maximum}")