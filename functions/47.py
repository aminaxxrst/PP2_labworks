#legb role: l-local, e-enclosing, g-global, b-built-in
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x) 
  inner() #Inner: local
  print("Outer:", x) 

outer() #Outer: enclosing
print("Global:", x) #Global: global
