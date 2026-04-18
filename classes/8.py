#default values in __init__, like argument in init takes some value
class Person:
    def __init__(self, name, age=18):
        self.name=name
        self.age=age

p1=Person("Emil")
p2=Person("Tobias", 25)

print(p1.name, p1.age) #Emil 18
print(p2.name, p2.age) #Tobias 25