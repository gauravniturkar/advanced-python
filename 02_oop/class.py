#this is supposed to be the blueprint for the Employee class

# class Employee: -> class definition starts with the keyword 'class' followed by the class name 'Employee' and a colon.
#     pass

# employee_1= Employee() -> instance creation
# employee_2= Employee()

# employee_1.name= "Alice"
# employee_1.position= "Developer"
# employee_1.salary= 80000

# employee_2.name= "Bob"
# employee_2.position= "Designer"
# employee_2.salary= 70000

# print(employee_1.name)
# print(employee_2.position)

#these above print statements are risky as they assume the attributes exist and we are repeating code. 



class Employee:
    # _init_ ek special method hai (also called "dunder method" - double underscore) jo Python mein constructor ka kaam karta hai.
    #  automatically called jab bhi aap class ka naya object/instance create karte ho. Iska main kaam hai object ko initialize karna with initial values.
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"

employee_1 = Employee()
employee_2 = Employee("Bob", "Designer", 70000)

print(employee_1.display_info())
print(employee_2.display_info())
