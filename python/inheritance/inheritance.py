
"""
Inheritance is the capability of one class to derive or inherit the properties from another class.
The class that derives properties is called the derived class or base class and the class from which the properties are being derived is called the base class or parent class.
The benefits of inheritance are:

It represents real-world relationships well.
It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
"""

# Parent class
class Person(object):

    # __init__ is known as constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class Employee(Person):
    def __init__(self, name, idnumber, post, salary):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print(f"My name is {self.name}")
        print(f"ID: {self.idnumber}")
        print(f"Post: {self.post}")
        print(f"Income: {self.salary}")

# creating of object or instance
a = Employee("Joshua Redding", 84641231079, "Intern", 20000)

# calling a function of the class Person using its instance
a.display()
a.details()
