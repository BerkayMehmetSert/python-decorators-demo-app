import math
import time


def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print(f"{func.__name__} took {finish - start} seconds")
    return inner

@calculate_time
def calculate_pow(x, y): 
    print(math.pow(x, y))


@calculate_time
def calculate_factorial(num):
    print(math.factorial(num))


@calculate_time
def calculate_add(x, y):
    print(x + y)


calculate_pow(2, 3)
calculate_factorial(5)
calculate_add(22, 23)
