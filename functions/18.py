#mixing positional and keyword arguments(kwargs), but positional arguments must come before kwargs
def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)
#I have a 5 year old dog named Buddy

my_function("dog", name="Buddy", age=5)