user_input = int(input('Provide me a number i will give you its Factorial: '))
count = user_input
factorial_of_user_input =1

while(count>0):
    factorial_of_user_input *=count
    count -= 1

print(f"{factorial_of_user_input} 'is the factorial of {user_input}")