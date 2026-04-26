#creating multiple objects to the same class
class MyClass:
    x=5

p1=MyClass()
p2=MyClass()
p3=MyClass()

print(p1.x) #5
print(p2.x) #5
print(p3.x) #5