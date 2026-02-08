#nonlocal variable belongs to the outer function
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello" #in this case x in myfunc1() is changed to "hello"
  myfunc2() 
  return x

print(myfunc1()) #hello