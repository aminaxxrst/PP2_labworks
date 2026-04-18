#**kwargs take those parameters as a dictionary
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
#His last name is Refsnes