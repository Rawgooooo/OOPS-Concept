
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
    def __init__(self, name, idnumber, salary, post):
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
a = Employee("Joshua Redding", 84641231079, 20000, "Intern")

# calling a function of the class Person using its instance
a.display()
a.details()
