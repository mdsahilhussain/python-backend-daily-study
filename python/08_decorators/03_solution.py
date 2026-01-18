import time

def cache(func):
    def wrapper(*args):
        cache_value ={}
        print(cache_value)
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_func(a,b):
    time.sleep(2)
    return a+b

print(long_running_func(4,5))
print(long_running_func(4,5))
print(long_running_func(9,5))
# long_running_func(4,5)
# long_running_func(4,5)
