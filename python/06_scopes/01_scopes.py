username = "chaiaurcode"

def print_username():
    username = "localuser"
    print("Inside function:", username)

print("Outside function:", username)
print_username()

x = 99
def func(y):
    z = x+y
    return z

result = func(1)
print("Result of func(1):", result)


count = 0
def increment():
    global count
    count += 1

increment()
print("Global count after increment:", count)


a = 99
def outer_function():
    a = 88
    def inner_function():
        print("Inner function a:", a)
    return inner_function

inner = outer_function()
print("inner function:",inner)
inner() 

def chai_coder(num):
    def actual_function(x):
        return x ** num
    return actual_function

square = chai_coder(2)
cube = chai_coder(3)

print("Square function object:", square)
print("Cube function object:", cube)

print("Square of 2:", square(2))
print("Cube of 2:", cube(2))