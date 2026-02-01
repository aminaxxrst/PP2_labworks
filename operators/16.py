#idenity operators- used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
x=["apple", "banana"]
y=["apple", "banana"]
z=x
print(x is z) #True
print(x is y) #False, their address are different
print(x==y) #True
#is returns True if both variables point to the same object