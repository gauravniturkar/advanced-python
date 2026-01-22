class Employee:
    raise_amount = 1.05  
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def apply_raise(self):
        self.salary += self.salary * Employee.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_str(cls, emp_str):
        name, position, salary = emp_str.split('-')
        return cls(name, position, int(salary))
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
employee_1 = Employee("Alice", "Developer", 80000)
employee_2 = Employee("Bob", "Designer", 70000)

# print("Before Raise:")
# print(employee_1.raise_amount)
# print(employee_2.raise_amount)    

# Employee.set_raise_amount(1.10)

# print("After Modifying Raise Amount via Class Method:")
# print(Employee.raise_amount)  # Accessing class variable via class name
# print(employee_1.raise_amount)  # Accessing class variable via instance
# print(employee_2.raise_amount)  # Accessing class variable via instance


emp_str_1 = "Charlie-Manager-90000"
emp_str_2 = "Diana-Analyst-60000"   

employee_3 = Employee.from_str(emp_str_1)
employee_4 = Employee.from_str(emp_str_2)

print("Employee 3 Info:", employee_3.name, employee_3.position, employee_3.salary)
print("Employee 4 Info:", employee_4.name, employee_4.position, employee_4.salary)

import datetime
my_date = datetime.date(2026, 1, 15)
print(Employee.is_workday(my_date))  # Using static method to check if a date is a workday



# class- regular methods automatically pass instance as first argument (self)
# class methods- automatically pass class as first argument (cls)
# static methods- don't pass anything automatically, behave like regular functions but belong to class namespace


# Static method ek aisa method hai jo:

# Na class ko access karta hai (cls nahi chahiye)
# Na instance ko access karta hai (self nahi chahiye)
# Bas ek utility function ki tarah kaam karta hai jo class ke andar organize hai
