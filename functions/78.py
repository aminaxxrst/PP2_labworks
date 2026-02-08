def simple_gen():
  yield 1
  yield 2

gen = simple_gen()
print(next(gen)) #1
print(next(gen)) #2
print(next(gen)) # This will raise StopIteration