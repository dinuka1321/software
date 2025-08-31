size = float(input("enter the zander size : "))
difference = 0
if size>=42:
    print("zander proves the limit, you can keep it ")
else:
    difference = float( 42 - size )
    print(f"the zander is {difference:4.2f} cm below the limit")