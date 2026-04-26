#title()- converts the first character of each word to upper case
s="amina KAmila Symbat"
print(s.title()) #"Amina Kamila Symbat"

#translate()- оның өзінің жеке аудару кестесі болады, maketrans()
x="abc"
y="123"
table=str.maketrans(x, y)
s="Amina"
print(s.translate(table)) #Amin1

dictionary={'a':'1', 'b':'2', 'c':'3'}
table=str.maketrans(dictionary)
s="Amina"
print(s.translate(table)) #Amin1

x="abc"
y="123"
table=str.maketrans(x, y, 'n')
s="Amina"
print(s.translate(table)) #Ami1