#order of arguments/parameters: regular -> *args -> **kwargs
def my_function(title, *args, **kwargs):
  print("Title:", title) #Title: User Info
  print("Positional arguments:", args) #Positional arguments: ()'Emil', 'Tobias')
  print("Keyword arguments:", kwargs) #Keyword arguments: {'age':25, 'city':'Oslo'}

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")