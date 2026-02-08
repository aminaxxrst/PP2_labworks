#secure th dunction with *args and **kwargs
#decortor
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
#function
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John")) #HELLO JONN