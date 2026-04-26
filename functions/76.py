def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen)) #0
print(next(gen)) #1
print(next(gen)) #2
#next()- iterator