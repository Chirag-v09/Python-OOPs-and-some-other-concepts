# Two types of decorators
# function decorators and
# class decorators

import functools


def start_and_end_decorator(n):
    print(n)

    def decorator(abc):
        print(n)
        @functools.wraps(abc)
        # to preserve the information about used function i.e when we use func.__name__ then it will show func name
        def wrapper(*args, **kwargs):
            print(n)
            for _ in range(n):
                result = abc(*args, **kwargs)
            return result
        print(n)
        return wrapper
    print(n)
    return decorator


@start_and_end_decorator(3)
def add_5(x):
    print(x)


add_5(5)
