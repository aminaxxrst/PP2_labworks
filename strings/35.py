#find(value, start, end)- returns the position of first occurence of substring, -1 if not found
s="Aminana"
print(s.find('a')) #4
print(s.find('T')) #-1 
print(s.find('n', 3, 6)) #3 in [3, 6], 'nan'

#format()- {} is replace by a value
s="My name is {}, I am {} years old"
print(s.format("Amina", 18)) #My name is Amina, I am 18 years old
#with index
s="My name is {1}, I am {0} years old"
print(s.format(18, "Amina")) #My name is Amina, I am 18 years old
#with variables
s="My name is {name}, I am {age} years old"
print(s.format(name="Amina", age=18)) #My name is Amina, I am 18 years old
#with modifiers
s="Pi equals {:.2f}"
print(s.format(3.14159265359)) #Pi equals 3.14, .2f means 2 digits after decimal point

#format_map()-it takes a values from a dictionary
person={'name':'Amina', 'age':18}
s="My name is {name}, I am {age} years old"
print(s.format_map(person)) #My name is Amina, I am 18 years old
print(s) #My name is {name}, I am {age} years old
#with format accesing values from dictionary, problem is if we don't have enough info, it gives an error
print(s.format(**person)) #My name is Amina, I am 18 years old