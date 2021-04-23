
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
