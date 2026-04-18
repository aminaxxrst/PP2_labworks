#adding new property to an object
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25 #age and city are new properties for p1 object
p1.city = "Oslo"

print(p1.name) #Tobias
print(p1.age) #25
print(p1.city) #Oslo