user_input = int(input("Provide a number: "))

if user_input > 1:
    for i in range(2, user_input):
        if(i % 2 != 0):
            print('this {user_input} number is prime')
        break