def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen)) #Emil
print(next(gen)) #Tobias
print(next(gen)) #Linus