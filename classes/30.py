#for creating child class you have to send a parent class as a parameter to the child class
class Person:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    
    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    pass

x=Student("Mike", "Olsen") #fname=Mike, lname=Olsen
x.printname() #Mike Olsen