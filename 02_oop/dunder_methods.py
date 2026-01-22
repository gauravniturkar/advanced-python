class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        return f"{self.name} is working as a {self.position}."
    
    def __repr__(self):
        return f"Employee(name='{self.name}', position='{self.position}')"  
    
    def __str__(self):
        return f"{self.name}, the {self.position}"  
    
    def __add__(self, other):
        if isinstance(other, Employee):
            return f"{self.name} and {other.name} are collaborating."
        return NotImplemented
    
    def __len__(self):
        return len(self.name) + len(self.position)
    

# Example usage:
emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Designer")
print(repr(emp1))  # Output: Employee(name='Alice', position='Developer')
print(str(emp1))   # Output: Alice, the Developer

print(emp1.__repr__())  # Output: Employee(name='Alice', position='Developer')
print(emp1.__str__())   # Output: Alice, the Developer


print(1+2)

print(int.__add__(1, 2))  # Output: 3
print(str.__add__("Hello, ", "World!"))  # Output: Hello, World!

print(emp1 + emp2)  # Output: Alice and Bob are collaborating.



print(len('test'))

print('test'.__len__())  # Output: 4

