age =  input("Provide me an age: ")
age_in_int = int(age)

if  age_in_int < 13:
    print("Child")
elif age_in_int <20:
    print("Teenager")
elif age_in_int <51:
    print("Adult")
else:
    print("Senior")