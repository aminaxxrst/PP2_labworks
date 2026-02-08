#variable created inside a function can only be used inside that function, inside a function region is called local scope
def myfunc():
  x = 300
  print(x)

myfunc() #300