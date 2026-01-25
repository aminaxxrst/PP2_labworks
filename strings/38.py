#ljust(length, value)- left justify, бұл мәтінді сол жақ шетке түзеп (Left Justify), оң жағынан бос орындармен немесе арнайы таңбалармен толтыру арқылы мәтін ұзындығын белгілі бір мөлшерге жеткізетін әдіс
s="Amina"
print(s.ljust(10, '-')) #"Amina-----", len(Apple)=5, 10-5=5
print(s.ljust(2)) #"Amina", len(Apple)=5, it remains same, een the length in the function is smaller than length of the original string
print(s.ljust(10, '.'), "Almaty") #Amina.....Almaty"

#lower()- helps to make all characters from string to lower case
s="AMINA Is the BeSt"
print(s.lower()) #amina is the best
s="Amina 2007 ALMATY"
print(s.lower()) #amina 2007 almaty

#lstrip(value)- left strip, сол жақты тазарту
s="       Amina!  "
print("Result:", s.lstrip()) #"Result: Amina!  ", removing spaces for default from left side
s="abcbcaminaxxrst"
print(s.lstrip("abc")) #lstrip("abc") "abc" деген сөзді іздемейді, ол мәтіннің басында "a", "b" or "c" әріптерінің қайсысы болсада олар біткенше өшіреді
#"minaxxrst"
s="apptppat"
print(s.lstrip("apt")) #""