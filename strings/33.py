#capitalize()- makes first character to upper case
s="amina"
print(s.capitalize()) #Amina

#casefold()- makes string to lower case
s="AmINA"
print(s.casefold()) #amina

#center(length, character)- returns a centered string
s="book"
s1=s.center(10) #10-4=6/2=3, 3 spaces
print(f"'{s1}'") #'   book   '

s="book"
s1=s.center(20, '-') #20-4=16/2=8
print(s1) #--------book--------

s="Amina"
print(s.center(4)) #Amina note:it doesn't cut the word if in center the length of word is smaller than original string

#count(value, start, end)-count of substring that occured in string
s="Aminaaa"
print(s.count('a')) #3
print(s.count('A')) #1, case-sensitive, a is not A
print(s.count('a', 2, 5)) #1 a in (2,5) 'ina'
s="ababaaba"
print(s.count('ab')) #3