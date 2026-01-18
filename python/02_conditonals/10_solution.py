animal_name = input("Enter the name of an animal: ").lower()
animal_age = int(input("Enter the age of the animal: "))

if animal_age >=2:
    print(f"Senior {animal_name} food.")
elif animal_name == 'dog':
    print("Puppy food.")
elif animal_name == 'cat':
    print("Kitten food.")
else:
    print(f"baby {animal_name} food.")

    