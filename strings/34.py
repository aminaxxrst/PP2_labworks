#encode()- returns a byte version o the string
s="Hello"
print(s.encode()) #b'Hello', b means bytes
s="Сәлем"
print(s.encode()) #b'\xd0\xa1\xd3\x99\xd0\xbb\xd0\xb5\xd0\xbc'
s="ABC"
s1=s.encode()
print(s1.hex())  #414243, as 41=4*16+1=65(A), 42=4*16+2=66(B), 43=4*16+3=67(C)

#endswith(suffix, start, end)- checks if string ends with suffix (true, false)
#endswith((suffix1, suffix2, ... ), start, end)- returns true if string ends with any of the given suffixes
s="amina@gmail.com"
print(s.endswith('@gmail.com')) #True
print(s.endswith('.ru')) #False
print(s.endswith(('@gmail.com', '.ru'))) #True, we write suffixes in a tuple (), if we don't do that, it will consider that as a start index 
print(s.endswith('a', 0, 5)) #True, 'amina' ends with 'a' in [0,5)

#expandtabs(tabsize)- мәтін ішінде tab(\t) белгілерін бос орындарға ауыстырады, по дефолту 8, ауыстырып қана қоймай кесте түрінде әдемілеп береді
print("A\tB".expandtabs(4)) #"A"(1 әріп)+3 бос орын->"B" 4-орынға түседі
print("AA\tB".expandtabs(4)) #"AA"(2 әріп)+2 бос орынө>"B" 4-орынға түседі
print("AAA\tB".expandtabs(4)) #"AAA"(3 әріп)+1 бос орын->"B" 4-орынға түседі
'''
Answer:
A   B
AA  B
AAA B
expandtabs тағы tabsize как будто келесі стринг қай позицияда жазылатынын көрсететін секілді

difference with replace
print("A\tB".replace('\t',' '))
print("AA\tB".replace('\t', ' '))
Answer:
A B
AA B
'''