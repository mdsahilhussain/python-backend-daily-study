import time

def timer(func):
    def warper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"function call by - {func.__name__}")
        return [ f"start time - {start}", result, f"end time - {end}"]
    return warper

@timer
def example_func(num):
    time.sleep(num)

print(example_func(2))