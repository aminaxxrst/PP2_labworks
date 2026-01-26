#maketrans(value, removed value)- replace() секілді, бірақ 10-15 түрлі таңбаны бірге ауыстыру үшін
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