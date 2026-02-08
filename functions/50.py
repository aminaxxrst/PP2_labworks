#functions with variale can also be decorated
#decorator
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
#function
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John")) #HELLO JOHN