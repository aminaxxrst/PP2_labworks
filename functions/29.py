#*args and **kwargs allow functions to accept a unknown number of arguments
#*args- tuple of arguments, if you don't know how many arguments you will use
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#The youngest child is Linus