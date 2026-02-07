def my_function(*args):
  print("Type:", type(args)) #Type: <class 'tuple'>
  print("First argument:", args[0]) #First argument: Emil
  print("Second argument:", args[1]) #Second argument: Tobias
  print("All arguments:", args) #All arguments: ('Emil', 'Tobias', 'Linus')

my_function("Emil", "Tobias", "Linus")