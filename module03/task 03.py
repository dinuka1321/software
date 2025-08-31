gender = str(input("enter your gender : "))
gender = gender.upper()
hemoglobin = int(input("enter your hemoglobin count : "))

if gender =="F" and 117 < hemoglobin < 155:
    print(" normal")
elif gender == "F" and hemoglobin < 117:
    print("your hemoglobin level is low")
elif gender == "F" and hemoglobin >155:
    print(" your hemoglobin level is high")
elif gender == "M" and 134 <= hemoglobin <= 167:
    print(" your hemoglobin level is normal")
elif gender == "M" and 134 > hemoglobin:
    print(" your hemoglobin level is law")
elif gender == "M" and hemoglobin > 167:
    print(" your hemoglobin level is high")
else:
    print("invalid input")
