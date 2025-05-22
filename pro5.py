import pymongo


class Person:      # 1. Defines a class named Person (the blueprint for creating objects)
  def __init__(self, fname, lname):  # 2. Constructor method that initializes new Person objects
    self.firstname = fname     #Initialize the Person with specific attributes.

    self.lastname = lname   # 4. Assigns the lname argument to the instance variable lastname

  def printname(self):  # 5. Defines a method to print the full name
    print(self.firstname, self.lastname)  # 6. Prints the first and last name

class Student(Person):  # 7. Defines a Student class that inherits from Person
  def __init__(self, fname, lname, year):  # 8. Constructor for Student with additional year parameter
    super().__init__(fname, lname)  # 9. Calls the parent class's __init__ method
    self.graduationyear = year  # 10. Adds a new instance variable graduationyear

  def welcome(self):  # 11. Defines a welcome method specific to Student
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)  # 12. Prints welcome message with graduation year

x = Student("Sultan", "Ahmed", 2025)  # 13. Creates a Student object with name and graduation year
x.welcome()  # 14. Calls the welcome method on the Student object