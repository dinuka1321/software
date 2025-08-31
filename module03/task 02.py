cab_class = str(input("Enter your cabin class : "))
cab_class = cab_class.upper()
if cab_class =="LUX":
    print("you have a upper-deck cabin with a balcony")
elif cab_class == "A":
    print("you have a cabin above the car deck, equipped with a window")
elif cab_class == "B":
    print("you have a windowless cabin above the car deck")
elif cab_class == "C":
    print("you have a windowless cabin below the car deck")
else:
    print("invalid cabin class ")