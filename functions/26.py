#if you have only kwargs(keyword argument), should use "*, " before arguments
def my_function(*, name):
    print("Hello", name) #Hello Emil

my_function(name="Emil")