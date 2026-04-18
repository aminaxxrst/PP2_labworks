#__init__() method with multiple parameter, function in a class-method
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name) #Linus
print(p1.age) #30
print(p1.city) #Oslo
print(p1.country) #Norway