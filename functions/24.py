#if you have only positional argument, should use ", /"
def my_function(name, /):
    print("Hello", name) #Hello Emil

my_function("Emil")