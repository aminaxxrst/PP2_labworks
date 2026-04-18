#for inheriting __init__ method() from parents' class
class Person:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    
    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x=Student("Emil", 18)
x.printname() #Emil 18