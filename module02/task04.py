num1 = int(input("Enter number 01 : "))
num2 = int(input("Enter number 02 : "))
num3 = int(input("Enter number 03 : "))

total = int(num1+num2+num3)
average = float(total/3)
product = int(num1*num2*num3)

print("Total is : ", total)
print(f"Average is : {average:.3f}")
print("Product is : ",product)