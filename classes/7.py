#without the __init__() method, you would need to set properties manually for each object
class Person:
    pass

p1=Person()
p1.name="Emil"
p1.age=36

print(p1.name) #Emil
print(p1.age) #36