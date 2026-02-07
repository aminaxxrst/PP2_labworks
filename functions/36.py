#regular arguments with **kwargs, regular parameters must come before **kwargs
def my_function(username, **details):
  print("Username:", username) #Username: emil123
  print("Additional details:") #Additional details:
  for key, value in details.items(): 
    print(" ", key + ":", value)
    #  age: 25
    #  city: Oslo
    #  hobby: coding

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")