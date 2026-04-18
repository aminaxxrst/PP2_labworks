#you can access object properties using dot notation
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand) #Toyota
print(car1.model) #Corolla