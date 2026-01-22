class Employee:
    
    raise_percentage = 1.05  # Class variable shared by all instances
    
    def apply_raise(self):
        self.salary += self.salary * Employee.raise_percentage
    
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"
    

employee_1 = Employee("Alice", "Developer", 80000)
employee_2 = Employee("Bob", "Designer", 70000)

# print("Before Raise:")
# print(employee_1.salary)
# print(employee_2.salary)

employee_1.apply_raise()
employee_2.apply_raise()

# print("After Raise:")
# print(employee_1.salary)
# print(employee_2.salary)       


# print(Employee.raise_percentage)  # Accessing class variable via class name
# print(employee_1.raise_percentage)  # Accessing class variable via instance
# print(employee_2.raise_percentage)  # Accessing class variable via instance


# print(Employee.__dict__)  # Displays instance attributes as a dictionary



Employee.raise_percentage = 1.10  # Modifying class variable

print("After Modifying Raise Percentage:")
# employee_1.apply_raise()
print(Employee.raise_percentage)


employee_1.raise_percentage = 1.15  # Instance variable, shadows class variable for this instance

print("After Setting Instance-specific Raise Percentage:")
print(employee_1.raise_percentage)  # Instance variable
print(employee_2.raise_percentage)  # Still refers to class variable