def gall_liters(gallons):
    return gallons * 3.78541

def main():
    gallons = float(input("Enter gallons (negative to stop): "))
    while gallons >= 0:
        liters = gall_liters(gallons)
        print(f"{gallons} gallons = {liters:.2f} liters")
        gallons = float(input("Enter gallons (negative to stop): "))

main()