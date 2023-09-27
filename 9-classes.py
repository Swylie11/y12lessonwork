# Sam Wylie, 27/9/2023
# Introduction to classes

class Employees:
    """ Create a new class with the names of employees """
    def __init__(self, name, surname, department, years):
        self.name = name
        self.surname = surname
        self.department = department
        self.experience = years
        self.salary = 0

    def setSalary(self):
        if self.experience <= 5:
            self.salary = 50000
        elif 10 >= self.experience > 5:
            self.salary = 100000
        else:
            self.salary = 120000
        return self.salary


newEmp = Employees('Sam', 'Wylie', 'Software', 2)
print(newEmp.salary)

print(f"New employee is {newEmp.name} {newEmp.surname}. They have {newEmp.experience} "
      f"years of experience in {newEmp.department}. "
      f"Starting salary is {newEmp.setSalary()}")
