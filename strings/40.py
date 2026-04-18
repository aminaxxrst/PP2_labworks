#partition()- мәтінді белгілі бір сөз немесе таңба арқылы қақ бөліп, 3 бөліктен тұратын tuple жасайды
s="name=Amina"
print(s.partition('=')) #('name', '=', 'Amina')

#if there is no separator then first element in tuple just the text, other elements are empty
s="name=Amina"
print(s.partition('age')) #('name=Amina', '', '')

s="abilmazhinova07@mail.ru"
user, separator, domain=s.partition('@') #user='abilmazhinova07', separator='@', domain='mail.ru'
print('User:', user)
print('Domain:', domain)
#User: abilmazhinova07
#Domain: mail.ru

#difference with split()
s="Amina-Kamila-Symbat"
print(s.split('-')) #['Amina', 'Kamila', 'Symbat']
print(s.partition('-')) #('Amina', '-', 'Kamila-Symbat')