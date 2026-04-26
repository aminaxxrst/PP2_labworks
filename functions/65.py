#lambda with sorted
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students) #[('Tobias', 22), ('Emil', 25), ('Linus', 28)]
#it's incorrect output: [(22, "Tobias"), (25, "Emil"), (28, "Linus")]

#tuples in the list, it sorted list by the age, but elements stay same