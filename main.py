#   1. Encapsulation
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # public attribute
        self.__balance = balance  # private attribute (double underscore)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):  # getter method
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(100)
print(account.get_balance())  # 1300
# print(account.__balance)  # Error - private attribute





#  2. Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!





#   3. Polymorphism
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(4, 5), Circle(7)]

for shape in shapes:
    print(f"Area: {shape.area()}")  # Same method name, different implementations




#    4. Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract class
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started - engine running")
    
    def stop(self):
        print("Car stopped - engine off")

class Bike(Vehicle):
    def start(self):
        print("Bike started - pedaling")
    
    def stop(self):
        print("Bike stopped - brakes applied")

# vehicle = Vehicle()  # Error - can't instantiate abstract class
car = Car()
car.start()  # Car started - engine running






