#**kwargs  parameter allows a function to accept any number of keyword arguments.
def my_function(**myvar):
  print("Type:", type(myvar)) #Type: <class 'dict'>
  print("Name:", myvar["name"]) #Name: Tobias
  print("Age:", myvar["age"]) #Age: 30
  print("All data:", myvar) #All data: {'name':'Tobias', 'age'=30, 'city'='Bergen'}

my_function(name = "Tobias", age = 30, city = "Bergen")