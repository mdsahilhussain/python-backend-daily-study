def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_kwargs(name="shakiman", power="lazer")
print_kwargs(name="shakiman")
print_kwargs(name="shakiman", power="lazer", enemy="dr. jackaal")
