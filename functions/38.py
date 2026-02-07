#Unpacking arguments
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
print(my_function(*numbers)) # Same as: my_function(1, 2, 3)
#a=1, b=2, c=3