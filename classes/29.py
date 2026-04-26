#parent class- is the class being inherited from, also called base class
#child class- is the class that inherits from another class, also called derived class
#any class can be a parent class
class Person:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    
    def printname(self):
        print(self.fname, self.lname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe") #fname=John, lname=Doe
x.printname() #John Doe