password = input("Enter your password: ")

if len(password) < 6:
    print("Password is too weak.")
elif len(password) <= 10:
    print("Password is of medium strength.")
else:
    print("Password is strong.")