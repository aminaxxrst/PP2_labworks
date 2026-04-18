#properties defined inside __init__() belong to object properties(instance properties) and properties defined outside methods(functions) belong to class properties
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name) #Emil
print(p2.name) #Tobias
print(p1.species) #Human
print(p2.species) #Human