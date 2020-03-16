# Python Object-Oriented Programming


class Employee:
    """ Basic example of creating a class with constructor and instance method """

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# Example 1: use constructor to create object
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Gregory', 'Weiss', 60000)

print(emp_1.email)
print(emp_2.email)

# Example 2: use instance method
print(emp_1.fullname())
print(emp_2.fullname())


# Option 1 (Bad Way)
# - this works but is basically not object oriented
# class Employee:
#     pass

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Gregory'
# emp_2.last = 'Weiss'
# emp_2.email = 'gweiss27@gmail.com'
# emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)
