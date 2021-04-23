
def foo(a, b, *args, **kwargs):  # args is tuple and kwargs is dictionary

    print(a, b)
    print(args)
    for arg in args:
        print(arg)

    print(kwargs)
    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, six = 6, seven = 7)
print("\n#####\n")


def foo(a, b, *, c, e, k):  # all parameters after * are keyword only parameter i.e keyword argument
    print(a)
    print(b)
    print(c)
    print(e)
    print(k)


foo(1, 2, c=3, e=4, k=5)  # provide parameter names here to pass the value to them which are written after *.
print("\n#####\n")


def foo(a, b, c):
    print(a, b, c)


my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
foo(*my_tuple)
foo(*my_list)
# here * is use to unpack the list & tuple to the pass the list & tuple items as arguments
# and the only condition is that the number of items in list or tuple is equal to number of parameters
my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)
# here ** is use to unpack the dict to the pass the dict values as arguments
# and the condition is that the number of keys in dict is equal to number of parameters
# also the key should match to parameter name.
print("\n#####\n")


