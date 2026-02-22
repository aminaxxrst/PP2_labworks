class MyNumbers:
  def __iter__(self):
    self.a = 1 #a=1
    return self

  def __next__(self):
    x = self.a #x=1
    self.a += 1 #a=2
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter)) #1
print(next(myiter)) #2
print(next(myiter)) #3
print(next(myiter)) #4
print(next(myiter)) #5