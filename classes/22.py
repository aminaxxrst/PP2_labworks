#all methods should have "self" as a first parameter, then they can use multiple parameters
class Calculator:
  def add(self, a, b): #add()- method
    return a + b

  def multiply(self, a, b): #multiply()- method
    return a * b

calc = Calculator() #calc-object
print(calc.add(5, 3)) #8
print(calc.multiply(4, 7)) #28