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

class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

        p1 = Person
        print(p1.age)    

