your_number = int(input("Enter a number: "))
sum_of_evens = 0
for i in range(1, your_number + 1):
    if(i % 2 == 0):
        sum_of_evens += i
print("The sum of even numbers from 1 to", your_number, "is:", sum_of_evens)