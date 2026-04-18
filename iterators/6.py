#In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration #when a=21, the iteration willstop and raise an error

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x) #from 1 to 20