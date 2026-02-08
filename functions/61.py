def myfunc(n): #n=3
  return lambda a : a * n

mytripler = myfunc(3) #a*3

print(mytripler(11)) #11*3=33
#mytripler as a lambda function, you should give a parameter to this