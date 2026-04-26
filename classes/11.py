#the self parameter must be the first parameter of any method in the class (in every function)
class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname() #Tobias
p2.printname() #Linus