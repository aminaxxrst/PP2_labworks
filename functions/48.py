#define the decorator first, then apply it with @decorator_name above the function
#decorator
def changecase(func): #func=myfunction
  def myinner():
    return func().upper() #HELLO SALLY
  return myinner #HELLO SALLY

@changecase
#function
def myfunction():
  return "Hello Sally"

print(myfunction()) #HELLO SALLY