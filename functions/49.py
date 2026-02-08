#using decorator multiple times
#decorator
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
#function1
def myfunction():
  return "Hello Sally"

@changecase
#function2
def otherfunction():
  return "I am speed!"

print(myfunction()) #HELLO SALLY
print(otherfunction()) #I AM SPEED