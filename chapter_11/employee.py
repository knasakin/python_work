class Employee:
    def __init__(self, firstname: str, lastname: str, annual_salary: int):
        self.firstname = firstname
        self.lastname = lastname
        self.annual_salary = annual_salary

    def give_raise(self, increase=5000):
        self.annual_salary += increase
