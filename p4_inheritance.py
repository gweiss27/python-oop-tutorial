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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        self.email = first + '.' + last + '@gmail.com'


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


print("* Example 1: Simple inheritance *")

dev_1 = Developer('Corey', 'Schafer', 50000, None)
dev_2 = Developer('Gregory', 'Weiss', 60000, None)

print(dev_1.email)
print(dev_2.email)

# print(help(Developer))

print("* Example 2: Change Subclass value (raise_amount) *")

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print("* Example 3: Calling super() constructor *")

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Gregory', 'Weiss', 60000, 'Java')

print("* Example 4: Another Subclass holding subclass *")

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
mgr_1.print_emps()
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Developer))
print(isinstance(mgr_1, Employee))
print(issubclass(Manager, Employee))

