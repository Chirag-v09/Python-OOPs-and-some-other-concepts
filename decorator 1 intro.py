# Two types of decorators
# function decorators and
# class decorators

def start_and_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper


def print_name():
    print("Chirag")


print_name_ = start_and_end_decorator(print_name)
print_name_()


@start_and_end_decorator
def print_name2():
    print("Rahul")


print_name2()
