your_number = int(input('Enter a number: '))

for i in range(1, 11):
    if(i == 5):
        continue
    result = your_number * i
    print(f"{your_number} X {i} = {result}")

