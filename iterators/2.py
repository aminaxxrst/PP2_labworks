#Strings are also iterable objects, containing a sequence of characters
mystr = "banana"
myit = iter(mystr)

print(myit) #<str_ascii_iterator object at 0x00000237E1FB9150>
print(next(myit)) #b
print(next(myit)) #a
print(next(myit)) #n
print(next(myit)) #a
print(next(myit)) #n
print(next(myit)) #a