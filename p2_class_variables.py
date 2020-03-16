# Python Object-Oriented Programming


class Employee:
    """ Basic example demonstrating class variables, such as raise_amount """

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


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Gregory', 'Weiss', 60000)

# Example 1: class variable, each of these work
# Employee - class itself
# emp_1, emp_2 - instance of class with a class var
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Example 2: Change CLASS variable
print("* Change CLASS variable")
Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Example 3: Change Class INSTANCE value
print("* Change CLASS INSTANCE variable")
Employee.raise_amount = 1.04  # reset to original value
emp_1.raise_amount = 1.05

# print namespace of emp_1
print("** Print NAMESPACE **")
print(emp_1.__dict__)
print(Employee.__dict__)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# Example 4: CLASS variable
# - 2 increments once each time an employee is created
print(Employee.num_of_emps)
