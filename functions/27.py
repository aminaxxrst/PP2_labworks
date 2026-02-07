#if you write "*, " before a positional argument, you will get an error
'''
def my_function(*, name):
    print("Hello", name)
my_function("Emil")
'''