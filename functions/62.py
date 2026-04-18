def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #a*2
mytripler = myfunc(3) #a*3

print(mydoubler(11)) #11*2=22
print(mytripler(11)) #11*3=33