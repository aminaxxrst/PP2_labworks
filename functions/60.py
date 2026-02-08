def myfunc(n): #n=2
  return lambda a : a * n

mydoubler = myfunc(2) #a*2

print(mydoubler(11)) #11*2=22
#mydoubler as lambda function, you should give a parameter to this