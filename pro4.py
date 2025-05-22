# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:  # Create a class named Person, with  properties name and age:

  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Sultan", 36)  #  Create an object named p1, and assign values for name and age:
print(p1.name)  #  print the value of name
print(p1.age)   #  print the value of age



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

sultan = Person("Sultan", 80)
faizan = Person("Faizan", 30)
usman = Person("Usman", 27)
arsalan = Person("Arsalan", 18)
print(sultan.name)
print(faizan.name)
print(usman.name)
print(arsalan.name)
print(sultan.age)



