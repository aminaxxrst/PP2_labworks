#if you use ", /" his with kwargs(keyword arguments), you will get an error
'''
def my_function(name, /):
    print("Hello", name)

my_function(name="Emil")
'''