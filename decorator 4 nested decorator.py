# Three conversion flags are currently supported: '!s' which calls str() on the value, '!r' which calls repr()
# and '!a' which calls ascii().
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


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
@start_and_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


say_hello('Chirag')


