class Person:     
     
     # 1. Now we can use the class named Person to create objects: 
     # This line defines a blueprint called "Person" for creating objects. 
     # Think of it like a cookie cutter that can make
     #  many cookies (objects) with the same shape.



     
     def __init__(self, name, age):  
          

        # 2. This is a special method called the constructor.  
        #   It's automatically called when you create a new object from the Person class.
        #  "self" refers to the instance of the object being created, and "name" and "age" are 
        #   parameters you provide when creating a Person object.
        #



       self.name = name            
   # 3. Here, we are assigning the value passed as the "name" parameter (in the constructor)
    #  to an attribute called "name" of the object being created ("self"). 
    # So, each Person object will have its own "name".




       self.age = age           


      # 4. Similarly, this line assigns the value passed as the "age" parameter to an attribute 
      # called "age" of the current Person object ("self"). 
      # Each Person object will also have its own "age".



     def myfunc(self):                
    # 5. This defines a regular method (a function associated with the class) called "myfunc".
    #  Again, "self" refers to the specific Person object this method is being called on.





      print("Hello my name is " + self.name)    
       # 6. Inside the "myfunc" method, this line prints a greeting along with the "name" attribute 
       # of the specific Person object that called this method.



p1 = Person("Sultan", 36)        
  # 7. This line creates a new object of the Person class and assigns it to the variable "p1". 
  # When this line executes, the __init__ method is automatically called with "self" referring 
  # to the new object, "name" set to "Sultan", and "age" set to 36.





p1.myfunc()  
 # 8. This line calls the "myfunc" method on the "p1" object. 
 # So, it will execute the code inside "myfunc", and because "self.name" for "p1" is "Sultan", 
 # it will print "Hello my name is Sultan".