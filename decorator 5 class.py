
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_times = 0

    def __call__(self,  *args, **kwargs):
        self.num_times += 1
        print(f'This function is called {self.num_times} times')
        self.func(*args, **kwargs)


@CountCalls
def say_hello(name):
    print(f'Hello {name}')


say_hello('Chirag')
say_hello('Chirag')
