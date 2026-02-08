#decorator
def changecase(n): #n=1
  def changecase(func): #func=myfunction
    def myinner():
      if n == 1:
        a = func().lower() #a=hello linus
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
#function
def myfunction():
  return "Hello Linus"

print(myfunction()) #hello linus