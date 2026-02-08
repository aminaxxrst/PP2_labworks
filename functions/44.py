#using global inside a function
def myfunc():
  global x
  x = 300
  print(x)

myfunc() #300

print(x) #300