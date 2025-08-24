talent = int(input("enter talent : "))
pound = int(input("enter pounds : "))
lot = float(input("enter lots : "))

mass = float(((lot*13.3)+(pound*32*13.3)+(talent*20*32*13.3)))

killograms =  int(mass // 1000)
grams = float(mass % 1000)

print(f"The weight in modern units : {killograms:} killograms and {grams:2.2f} grams")