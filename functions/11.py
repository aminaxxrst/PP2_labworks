#if your function expects 2 arguments, you must call it with exactly 2 arguments
def my_function(fname, lname):
    print(fname+" "+lname)
my_function("Emil", "Refsnes")

'''
if you try this you will get an error
def my_function(fname, lname):
    print(fname+" "+lname)
my_function("Emil")
'''