#multiple decorators, decorators are called in the reverse order, starting with the one closest to the function
#decorator2
def changecase(func):
  def myinner():
    return func().upper() #HELLO TOBIAS HAVE A GOOD DAY!
  return myinner

#decorator1
def addgreeting(func): 
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner #Hello Tobias Have a good day!

@changecase #it will change the output from 1st decorator
@addgreeting #1st
#function
def myfunction():
  return "Tobias"

print(myfunction()) #HELLO TOBIAS HAVE A GOOD DAY!