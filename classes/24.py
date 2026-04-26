#method can change a property value
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1 #in this case this method changes p1.age property's value
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday() #Happy birthday! You are now 26
p1.celebrate_birthday() #Happy birthday! You are now 27