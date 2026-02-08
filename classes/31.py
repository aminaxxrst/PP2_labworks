#as we know every class must have __init__() method
class Person:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    
    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, course, age):
        self.course=course
        self.age=age
    
    def printinfo(self):
        print(self.course, self.age)

x=Student("IT", 18)
x.printinfo() #IT 18
#as children class(in this case Student) ha its own __init__ method() it overtakes parents' __init__ method()