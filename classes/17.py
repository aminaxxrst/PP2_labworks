#deleting property with a "del" keyword
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # Linus
# print(p1.age) # This would cause an error