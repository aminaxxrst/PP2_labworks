#split(sep, number)- мәтінді белгілі бір sep арқылы бөледі және тізімге салады
s="Amina=Kamila=Symbat"
print(s.split('=')) #['Amina', 'Kamila', 'Symbat']
print(s.split('=', 1)) #['Amina', 'Kamila=Symbat']
s="Amina Kamila Symbat"
print(s.split()) #['Amina', 'kamila', 'Symbat'], по дефолту sep=' '
s="abc d"
print(s.split()) #['abc', 'd']
print(list(s)) #['a', 'b', 'c', ' ', 'd']

#splitlines()- стрингты абзац-абзацқа бөліп, тізім жасау
s="Amina\nKamila\nSymbat\n"
print(s.splitlines()) #['Amina', 'Kamila', 'Symbat']
print(s.split('\n')) #['Amina', 'Kamila', 'Symbat', '']
print(s.splitlines(True)) #['Amina\n', 'Kamila\n', 'Symbat\n']

#startswith(value), startswith(value)- returns True if the string starts with the specified value/value1 or value2
s="Amina"
print(s.startswith('A')) #True

#strip(value)- мәтіннің ең басымен ең соңымен келеді егерде валудан тыс нәрсе болатын болса тоқтайды, болмаса өшіреді
s="banana ,. banana"
print(s.strip('ab')) #"nana ,. banan"
s="    Amina     "
print(len(s.strip())) #"Amina", answer: 5

#swapcase()- lower case become upper case and vice versa
s="Amina"
print(s.swapcase()) #aMINA
s="amina 18 KAMILA"
print(s.swapcase()) #AMINA 18 kamila