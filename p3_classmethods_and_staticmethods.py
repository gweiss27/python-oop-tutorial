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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first_local, last_local, pay_local = emp_str.split('-')
        return cls(first_local, last_local, pay_local)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Gregory', 'Weiss', 60000)

# Example 1: @classmethod
# here we call set_raise_amount which changes the value for all instances of a class

print("* Example 1: @classmethod *")
Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Example 2: Change @classmethod with an instance

print("* Example 2: @classmethod changing on an instance *")
emp_1.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Example 3: @classmethod as alternate constructor

print("* Example 3: @classmethod as alternate constructor *")
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

print(" -- without @classmethod")
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)

print(" -- with @classmethod")
print(Employee.from_string(emp_str_1))
print(Employee.from_string(emp_str_2))
print(Employee.from_string(emp_str_3))

# Example 4: @staticmethod
print("* Example 4: @staticmethod *")

import datetime
my_date = datetime.date(2020, 3, 14)
print(Employee.is_workday(my_date))

my_other_date = datetime.date(2020, 3, 16)
print(Employee.is_workday(my_other_date))

