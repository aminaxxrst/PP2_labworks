#walrus operator (:=)- it assigns values to variables as part of a larger expression
#the count variable is assigned in the if statement, and given the value 5
numbers=[1, 2, 3, 4, 5]
if (count:=len(numbers)) >3:
    print("List has,", count, "elements") #List has 5 elements

if count:=len(numbers)>3:
    print("List has,", count, "elements") #List has True elements