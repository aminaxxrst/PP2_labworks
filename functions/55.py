#when you decorate a function and use the __name__ atribute it returns the inner function from decorator
#decorator
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
#function
def myfunction():
  return "Have a great day!"

print(myfunction.__name__) #myinner