class Employee:
    def __init__(self,first,last,salary):
        self._first= first
        self._last= last
        self._salary= salary
    @property
    def email(self):
        return f"{self._first.lower()}.{self._last.lower()}@company.com"
    def fullname(self):
        return f"{self._first} {self._last}"
    
    @fullname.setter
    def fullname(self,name):
        first,last= name.split(" ")
        self._first= first
        self._last= last
    

emp_1 = Employee("John","Doe",50000)
print(emp_1.email)  # Output:

emp_1._first= "Jane"  # Directly modifying the _first attribute
# print(emp_1.email)  # Output will still show the old email since email property doesn't auto-update: