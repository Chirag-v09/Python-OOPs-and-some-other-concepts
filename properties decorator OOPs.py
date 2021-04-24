
# Objectives

# getter, setter
# getter -> @property
# setter -> @x.setter

class SoftwareEngineer:

    def __init__(self):
        self._salary = None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        # we can do checks, constraints, internal calculations here.
        self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary


se = SoftwareEngineer()

se.salary = 7000
print(se.salary)
del se.salary


