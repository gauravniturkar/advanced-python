class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        self.email = f"{name.lower().replace(' ', '.')}@company.com"

    def work(self):
        return f"{self.name} is working as a {self.position}."
    

class Developer(Employee):
    def __init__(self, name, position, salary, department):
        super().__init__(name, position, salary)
        # Employee.__init__(self, name, position, salaryq)  # Alternative way to call the parent constructor
        self.department = department

dev_1 = Developer("Alice", "Developer", 80000, "IT")
dev_2 = Developer("Bob", "Developer", 85000, "IT")
dev_3 = Developer("Charlie", "Developer", 90000, "IT")
dev_4 = Developer("Diana", "Developer", 95000, "IT")
dev_5 = Developer("Ethan", "Developer", 100000, "IT")

# print(dev_1.work())  # Output: Alice is working as a Developer.
# print(dev_1.department)


# print(help(Developer))  # Displays the method resolution order and inheritance details


class Manager(Employee):
    def __init__(self, name, position, salary, team_size, employee=None):
        super().__init__(name, position, salary)
        self.team_size = team_size
        if employee is None:
            self.employee = []
        else:
            self.employee = employee
    def add_employee(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)   
    
    def remove_employee(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)   

    def manage(self):
        return f"{self.name} is managing a team of {self.team_size} members."
    
    def print_employees(self):
        for emp in self.employee:
            print('-->', emp.name)
    
mgr_1 = Manager("Bob", "Manager", 95000, 10, [dev_1, dev_2, dev_3])
print(mgr_1.work())  # Output: Bob is working as a Manager.
print(mgr_1.manage())  # Output: Bob is managing a team of 10 members.

print("Employees under manager:")
mgr_1.print_employees()     

mgr_1.add_employee(dev_4)
print("Employees after adding one:")
mgr_1.print_employees()
mgr_1.remove_employee(dev_2)
print("Employees after removing one:")
mgr_1.print_employees()


print(isinstance(mgr_1, Developer))  # True
print(issubclass(Manager, Developer))  # True