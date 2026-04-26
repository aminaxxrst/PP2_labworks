#Regular arguments with *args, regular parameters must come before *args
def my_function(greeting, *names):
  for name in names:
    print(greeting, name) 
    #Hello Emil
    #Hello Tobias
    #Hello Linus

my_function("Hello", "Emil", "Tobias", "Linus")