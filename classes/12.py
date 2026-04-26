#self parameter doesn't have to be named "self", use whatever name of parameter, just it has to be first parameter of any method in the class
class Person:
  def __init__(amina, name, age):
    amina.name = name
    amina.age = age

  def greet(kamila):
    print("Hello, my name is " + kamila.name)

p1 = Person("Emil", 36)
p1.greet() #Hello, my name is Emil
