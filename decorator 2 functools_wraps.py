# Two types of decorators
# function decorators and
# class decorators

import functools


def start_and_end_decorator(func):

    @functools.wraps(func)
    # to preserve the information about used function i.e when we use func.__name__ then it will show func name
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


@start_and_end_decorator
def add_5(x):
    return x+5


print(add_5(5))

print()

result = add_5(10)
print(result)

print("\nHelp =")

print(help(add_5))
print("\nName=")
print(add_5.__name__)
