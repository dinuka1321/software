import math

def unit_price(diameter_cm, price):
    radius = diameter_cm / 2
    area_cm2 = math.pi * (radius ** 2)
    area_m2 = area_cm2 / 10000
    return price / area_m2

def main():
    d1 = float(input("Enter diameter of first pizza (cm): "))
    p1 = float(input("Enter price of first pizza (€): "))
    d2 = float(input("Enter diameter of second pizza (cm): "))
    p2 = float(input("Enter price of second pizza (€): "))

    unit1 = unit_price(d1, p1)
    unit2 = unit_price(d2, p2)

    print(f"First pizza unit price: {unit1:.2f} €/m²")
    print(f"Second pizza unit price: {unit2:.2f} €/m²")

    if unit1 < unit2:
        print("First pizza gives better value.")
    elif unit2 < unit1:
        print("Second pizza gives better value.")
    else:
        print("Both pizzas give the same value.")

main()