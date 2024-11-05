class Employee:
    def calculate_salary(self):
        print("Calculating generic employee salary")

class Manager(Employee):
    def calculate_salary(self):
        print("Calculating manager's salary with specific benefits")


emp = Employee()
mgr = Manager()
emp.calculate_salary()
mgr.calculate_salary()
