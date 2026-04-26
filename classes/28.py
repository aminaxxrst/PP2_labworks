#deleting methods with "del" keyword
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil") #name=Emil

del Person.greet

p1.greet() # This will cause an error