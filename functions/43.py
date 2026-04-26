#same variable name inside and outside of a function is 2 different variables
x = 300

def myfunc():
  x = 200
  print(x)

myfunc() #200

print(x) #300