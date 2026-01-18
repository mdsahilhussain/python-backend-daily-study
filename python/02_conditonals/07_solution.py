coffee_order = input("What size coffee would you like? (small/medium/large): ").lower()
is_with_extra_shot = input("Would you like to add an extra shot of espresso? (yes/no): ").lower()

if is_with_extra_shot == "yes":
    message = f"You have ordered a {coffee_order} coffee with an extra shot of espresso."
else:
    message = f"You have ordered a {coffee_order} coffee."

print(message)