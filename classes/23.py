#methods can use object properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old" #get_info() method uses p1.name and p1.age properties

p1 = Person("Tobias", 28)
print(p1.get_info()) #Tobias is 28 years old