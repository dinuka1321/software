length = float(input("Enter inches : "))

while length >= 0:
    cm = float(length * 2.54)
    print(f"{length:}inches is {cm:}cm ")
    length = float(input("enter inches : "))
print("invalid input")