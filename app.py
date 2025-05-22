#    ✅ 1. Encapsulation
class Person:
    def __init__(self, name, age, Id):
        self.name = name            # public
        self.__age = age            # private
        self._Id = Id               # confidentiole
    def show_info(self):
        print(f"My name is {self.name}  I am {self.__age} years old and My Id is {self._Id}")

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age

p = Person("Sultan", 25, 733)
p.show_info()
p.set_age(26)
p.show_info()



#   ✅ 2. Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting...")

class Car(Vehicle):  # Inheriting from Vehicle
    def open_trunk(self):
        print("Trunk opened.")

my_car = Car("Toyota")
my_car.start()
my_car.open_trunk()


#   ✅ 3. Polymorphism
class Bird:
    def speak(self):
        print("Some generic bird sound")

class Parrot(Bird):
    def speak(self):
        print("Parrot says: Hello!")

class Sparrow(Bird):
    def speak(self):
        print("Sparrow says: Chirp chirp!")

def animal_sound(bird):
    bird.speak()

p = Parrot()
s = Sparrow()

animal_sound(p)
animal_sound(s)






#   ✅ 4. Abstraction
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()

