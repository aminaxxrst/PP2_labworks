#changing value of class property(in this case lastname) affects all objects(p1 and p2)
class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname) #Refsnes
print(p2.lastname) #Refsnes