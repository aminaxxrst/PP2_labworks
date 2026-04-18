#methods= functions in a class
class Person:
  def __init__(self, name): #__init__()-method
    self.name = name

  def greet(self): #greet()-method
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet() #Hello, my name is Emil