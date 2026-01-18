def debug(func):
    def wrapper(*args, **kwargs):
        args_value = f', '.join(str(arg) for arg in args)
        kwargs_value = f', '.join(f"{k}:{v}" for k, v in kwargs.items())
        print(f"calling by: {func.__name__}")
        print(f"with argument value: [{args_value}] and")
        print(f"kw argument value: [{kwargs_value}]")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting = 'hello'): 
    print(f'{greeting}, {name} :)')


greet('chai', greeting='haan ji')