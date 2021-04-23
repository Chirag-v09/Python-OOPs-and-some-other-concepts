
my_list = [1, 2, 3, 4, 5, 6]
my_tuple = (1, 2, 3, 4, 5, 6)

*beg, last = my_list  # It will unpack the list into two parts the last item goes to the last variable and
# the rest of the elements except teh last will pass to beg variable.

print(beg)
print(last)
print("\n#####\n")

beg, *middle, last = my_tuple
print(beg)
print(middle)
print(last)
print("\n#####\n")

beg,second, *middle, second_last, last = my_tuple
print(beg)
print(second)
print(middle)
print(second_last)
print(last)
print("\n#####\n")


my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_set = {7, 8, 9}
# my_set = {4, 5, 6}

c_list = [*my_list, *my_tuple, *my_set]
# c_list = [*my_list, *my_set]
print(c_list)

my_dict1 = {'a': 1, 'b': 2}
my_dict2 = {'c': 3, 'd': 4}
c_dict = {**my_dict1, **my_dict2}
print(c_dict)


