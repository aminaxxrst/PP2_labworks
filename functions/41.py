#variable inside a function is available function inside the function, not outside the function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc() #300