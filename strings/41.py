#replace(old, new, number)- ескі сөзді жаңа сөзге ауыстырады, ал сан қанша ескі сөзді жаңа сөзге алмастыру кере екенін көрсетеді как лимит
s="Amina amina Kamila"
print(s.replace('Amina', 'Symbat')) #Symbat amina Kamila
s="amina amina amina"
print(s.replace('amina', 'kamila', 2)) #kamila kamila amina
print(s) #it doesn't change the original text
s='A m i n a'
print(s.replace(' ', '')) #Amina

#rfind(value, begin, end)- right find, last position of found string/symbol while find()-first position
s="amina amina kamila"
print(s.rfind('amina')) #6, as we have 2 amina, the last amina starts with 6th index
s="amina kamila"
print(s.rfind('symbat')) #-1, if there is no such value, it just returns -1
s="amina amina"
print(s.rfind('a', 4, 9)) #'a ami', starting with 4 index ending with 8 index, answer: 6

#rindex()- as a rfind, but if there is no value it returns ValueError
s="amina amina kamila"
print(s.rindex('amina')) #6
#s="amina kamila"
#print(s.rfind('symbat')) it returns ValueError
s="amina amina"
print(s.rindex('a', 4, 9))

#rjust(len of string, value)- right justify, мәтінді оң жаққа тіреп, сол жағын арнайы таңбамен толтырады
s="Amina"
print(s.rjust(10, '-')) #-----Amina
s="Amina"
print(s.rjust(2, '-')) #Amina

#rpartition(value)- partition() секілді бірақ value бірнеше рет кездессе соңғы валуды ортаға қойып, соғн байланыстыр стрингты екіге бөледіб егер біреу болса partition() дағыдай жауап
s="Amina=Kamila=Symbat"
print(s.partition('=')) #('Amina', '=', 'Kamila=Symbat')
print(s.rpartition('=')) #('Amina=Kamila', '=', Symbat')
print(s.rpartition('age')) #('', '', 'name=Amina')
s="name=Amina"
print(s.partition('=')) #('name', '=', 'Amina')
print(s.rpartition('=')) #('name', '=', 'Amina')

#rsplit(separator, number)- мәтінді separator бойынша бөледі, яғни 3 sep тапса, 4 стринг ин лист шығады, бірақ егер number жазбасақ partition() разница болмайды
s="Amina=Kamila=Symbat"
print(s.rsplit('=')) #['Amina', 'Kamila', 'Symbat']
print(s.split('=')) #['Amina', 'Kamia', 'Symbat']
print(s.rsplit('=', 1)) #['Amina=Kamila', 'symbat]

#rstrip(value)- right strip, по дефолту бос жолды, жаңа жолды өшіреді, ал егер мән берсек сол мәндегі әріптерді өшіреді
s="Amina     "
print(len(s.rstrip())) #"Amina", answer: 5
s="banana ,. banana"
print(s.strip('ab')) #"nana ,. banan", мәтіннің ең басынан және ең соңынан бастап тексер, егер кездескен әріп 'a' oe 'b' болса-өшір, егер басқа әріп кездессе-тоқта
print(s.rstrip('ab')) #"banana ,. banan" мәтіннің ең соңынан бастап тексер, егер кездескен әріп 'a' or 'b' болса-өшір, егер басқа әріп кездессе-тоқта
s="banana..,,cb"
print(s.rstrip(",.bc")) #"banana", мәтіннің ең соңынан бастап тексереді, егер кездескен әріп 'b', 'c', ',' or '.' болса-өшір, егер басқа әріп кездессе-тоқта