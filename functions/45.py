#in this case global x is changed inside of a function
x = 300

def myfunc():
  global x
  x = 200
  print(x)

myfunc() #200

print(x) #200