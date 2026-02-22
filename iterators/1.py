#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(myit) #<tuple_iterator object at 0x000001F46A7B8FD0>
print(next(myit)) #apple
print(next(myit)) #banana
print(next(myit)) #cherry