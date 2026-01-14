def even_generator(limit):
    for i in range(2, limit +1, 2):
        # return i - always return value, don't have other's reference.
        yield i # return value , and also store function and  state of function. 

for num in even_generator(10):
    print(num)