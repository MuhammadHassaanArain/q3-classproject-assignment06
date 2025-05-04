print("_______________________________________")

# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. 
# Use the self keyword to initialize these values via a
#constructor. Add a method display() that prints student details
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        
s1 = Student("Hassaan",87)
s2 = Student("Aasia", 88)
s1.display()
s2.display()
print("_______________________________________")


# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects
#  have been created. Use a class variable and a class method
#  with cls to manage and display the count.
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

obj1 =  Counter()
obj2 =  Counter()
obj3 =  Counter()
Counter.display_count()
print("_______________________________________")



# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public
#  method start(). Instantiate the class and access both from
#  outside the class.
class Car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} car is starting...")

my_car = Car("Toyota")
print("Brand: " , my_car.brand)
my_car.start()
print("_______________________________________")


# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a 
# class method change_bank_name(cls, name) that allows changing
#  the bank name. Show that it affects all instances.
class Bank:
    bank_name = "MCB"
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
bank = Bank()
print("Old Bank Name: " + bank.bank_name)
bank.change_bank_name("HBL")
print("New Bank Name: " + bank.bank_name)
print("_______________________________________")


# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b)
#  that returns the sum. No class or instance variables 
# should be used.
class MathUtils:
    @staticmethod
    def add(a , b):
        return a + b
    
result = MathUtils.add(2,4)
print(result)
print("_______________________________________")



# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object
#  is created (constructor) and another message when it is 
# destroyed (destructor).
class Logger:
    def __init__(self,):
        print("Logger object is created.")

    def __del__(self):
        print("Logger object is destroyed.")
obj = Logger()
del obj 
print("_______________________________________")


# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the
#  class and document what happens.
class Employee:
    def __init__(self,name, salary, ssn):
        self.name = name # Public Variable
        self._salary = salary # Protected Variable
        self.__ssn = ssn # Private Variable
    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self._salary}")
        print(f"Employee SSN: {self.__ssn}")
        

employee1 = Employee("Hassaan",10000,23456)
employee1.display() # this will corretly display the employee information.
print("--------------------")
print(f"Employee Name: {employee1.name}") # direct access to public variable.
print(f"Employee Salary: {employee1._salary}") # direct access to protected variable.
try: # trying to access the private variable directle (will raise an error)
    print(f"Employee SSN: {employee1.__ssn}")
except AttributeError as e:
    print(f"Error: {e}")
print("_______________________________________")

# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. 
# Inherit a class Teacher from it, add a subject field, and
#  use super() to call the base class constructor.
class Person:
    def __init__(self,name):
        self.name = name
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def  display_info(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

t1 = Teacher("Asghar","Mathematics")
t1.display_info()
print("_______________________________________")



# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with
#  an abstract method area(). Inherit a class Rectangle
#  that implements area().
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
rec1 = Rectangle(2,2)
print("Area of Rectangle: " , rec1.area())
print("_______________________________________")



# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. 
# Add an instance method bark() that prints a message 
# including the dog's name.
class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f" {self.name}, the {self.breed}, says: woof!")

dog1 = Dog("Herry","Italian")
dog1.bark()
print("_______________________________________")

# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. 
# Add a class method increment_book_count() to increase 
# the count when a new book is added.
class Book:
    total_books = 0
    def __init__(self):
        Book.increament_book_count()
    @classmethod
    def increament_book_count(cls):
        cls.total_books += 1

print(Book.total_books)
book1 = Book()
book2 = Book()
book3 = Book()
print(Book.total_books)
print("_______________________________________")


# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method 
# celsius_to_fahrenheit(c) that returns the Fahrenheit value.
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(cel):
        f = (cel * 9/5) + 32
        print(f"{cel}°C in Fahrenheit is {f}°F")
TemperatureConverter.celsius_to_fahrenheit(100)
TemperatureConverter.celsius_to_fahrenheit(44)
print("_______________________________________")


# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing
#  an Engine object to the Car class during initialization. Access
#  a method of the Engine class via the Car class.
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    def start(self):
        print(f"Engine with {self.horsepower} HP Started.")
class Car:
    def __init__(self, engine:Engine):
        self.engine = engine
    def start(self):
        print(f"Car is Starting...")
        self.engine.start() # accessing the engine method in car class

engine1 = Engine(528)
engine2 = Engine(1290)
car1 = Car(engine1)
car2 = Car(engine2)
car1.start()
car2.start()
print("_______________________________________")

# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use 
# aggregation by having a Department object store a reference
#  to an Employee object that exists independently of it.
class Employee:
    def __init__(self, name , emp_id):
        self.name = name 
        self.emp_id = emp_id
    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee
    def show_details(self):
        print(f"Department Name: {self.dept_name}")
        self.employee.display()

emp1 = Employee("Hassaan", 123)
dept1 = Department("IT",emp1)
dept1.show_details()

print("_______________________________________")

# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.
class A:
    def show(self):
        print("Calling from class A")
class B(A):
    def show(self):
        print("calling from class B")
class C(A):
    def show(self):
        print("calling from class c")
class D(B,C):
    def show(self):
        print("calling from class D")
objd = D()
objd.show()
print("_______________________________________")
