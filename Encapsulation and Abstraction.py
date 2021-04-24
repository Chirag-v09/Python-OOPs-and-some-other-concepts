
# Objective

# Encapsulation
# Abstraction
# Public, Private methods and attributes
# _foo(), _x
# getter, setter

class SoftwareEnginner:

    # if we use 1 underscore then that variable is protected and if we use 2 underscore then it is private
    # protected data member can be accessed from outside but we don't have to use them outside
    # private data member can accessed from outside
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None  # private attribute
        self._num_bugs_solved = 0  # private attribute

    def code(self):
        self._num_bugs_solved += 1

    # getter
    def get_salary(self):
        return self._salary

    # setter
    def set_salary(self, value):
        # check value, enforce constraints
        self._salary = self._calculate_salary(value)

    def _calculate_salary(self, base_salary):  # private function
        if self._num_bugs_solved < 10:
            return base_salary
        if self._num_bugs_solved < 100:
            return base_salary * 2
        return base_salary * 3


se = SoftwareEnginner('Chirag', 22)

print(se.name, se.age)
se.set_salary(7000)
print(se.get_salary())



