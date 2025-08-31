
attempts = 0

while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "python" and password == "rules":
        print("Welcome")
        break
    else:
        attempts += 1
else:
    print("Access denied")