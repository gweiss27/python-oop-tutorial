# Python Object-Oriented Programming


class Employee:
    """ Basic example demonstrating inheritance """

    num_of_emps = 0
    raise_amount = 1.04  # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps += 1  # no real use case to have instance of this value

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        """ 'Representation' - should be something that could be copied into the
        repl and recreate the object"""
        return "Employee('{}','{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        """ 'String' - meant to be more readable for an end-user """
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Gregory', 'Weiss', 60000)

print("* __repr__ *")
print(repr(emp_1))

print("* __str__ *")
print(str(emp_1))

print("* __add__ *")
print(1+2)
print(int.__add__(1, 2))

print("* Adding two Emps together *")
print(emp_1 + emp_2)


print("* __len__ *")
print(len('test'))
print('test'.__len__())

print("* Custom __len__ (length of fullname) *")
print(len(emp_1))
