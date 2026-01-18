age = input("Provide me an age:")
age_in_int = int(age)

day = input("Provide me an day:")

price = 12 if age_in_int >= 18 else 8

if day.lower() == "wednesday":
    price = price - 2

print("Ticket price for you is $",price)