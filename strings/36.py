#index()- returns the position of first occurence of substring, error if not found
s="Aminana"
print(s.index('a')) #4
#print(s.index('T')) #error
print(s.index('n', 3, 6)) #3 in [3, 6], 'nan'

#isalnum()- checks if all characters are alphanumeric (letters and numbers, A-z, 0-9), returns True or False
s="Amina2007"
print(s.isalnum()) #True
s="Amina"
print(s.isalnum()) #True
s="2007"
print(s.isalnum()) #True
s="Amina 2007"
print(s.isalnum()) #False, because it has the space which is not letter or number
s="amina@gmail.com"
print(s.isalnum()) #False, because of @ and .
s=""
print(s.isalnum()) #False, empty string

#isalpha()- checks if all characters are letters (A-z), returns True or False
s="Amina"
print(s.isalpha()) #True
s="Amina2@! "
print(s.isalpha()) #False, because of 2, @, ! and space
s=""
print(s.isalpha()) #False, empty string

#isascii()- checks if all characters are ASCII characters (characters with code between 0-127),returns True or False
s="Amina123! $@"
print(s.isascii()) #True
s="Сәлем, Амина!"
print(s.isascii()) #False, because of Cyrillic letters
s=""
print(s.isascii()) #True, empty string is considered as ASCII string

#isdecimal()- checks if all characters are decimal characters(0-9), returns True or False(power, -, +, ., space, letters)
s="12345"
print(s.isdecimal()) #True
s="-15.34" 
print(s.isdecimal()) #False, because of -, .
s="12 36"
print(s.isdecimal()) #False, because of space
s=""
print(s.isdecimal()) #False, because there is no number
s="2²"
print(s.isdecimal()) #False, because of power

#isdigit()- checks if all characters are digits, returns True or False(-, +, ., space, letters)
s="2²"
print(s.isdigit()) #True, it takes power as a digit, power=alt+0178
s="12345"
print(s.isdigit()) #True
s="-34.56"
print(s.isdigit()) #False

#isidentifier()- checks if string can be the name of variable or function, returns True or False
#it returns True, if it contins only A-z,0-9, _; the name shouldn't start with digit
print("my_variable".isidentifier()) #True
print("Var1".isidentifier()) #True
print("_hidden".isidentifier()) #True
print("Сәлем".isidentifier()) #True
print("2var".isidentifier()) #False, the name can't start with numbers
print("my-var".isidentifier()) #False, because of -
print("my var".isidentifier()) #False, because of space
#but there is a rule that name of variable can't be the Python keyword (if, class, def), but isidentifier() returns True, for them it doesn't matter
print("def".isidentifier()) #True

#islower()- checks if all characters in the string are lower case, returns True(хотя бы бір кішкентай әріп болу керек, стрингтағы барлық әріп кішкентай болу керек) or False
s="amina2007"
print(s.islower()) #True
s="2007"
print(s.islower()) #False
s="Amina"
print(s.islower()) #False

#isnumeric()- checks if all characters in the string are numeric(0-9), returns True or False(letters, space, -, .)
s="½"
print(s.isnumeric()) #True, because it's fraction
s="2²"
print(s.isnumeric()) #True, because it's power
s="-12.34"
print(s.isnumeric()) #False,because of -, .
s="十"
print(s.isnumeric()) #True, because it's 10 in Chinese numeric

#isprintable()- checks if all characters in string are printable, returns True or False(\n, \t)
s="Amina2007"
print(s.isprintable()) #True
s=" "
print(s.isprintable()) #True, because space is printable
s=""
print(s.isprintable()) #True, because empty string doesn't matter
s="Amina\n\t2007"
print(s.isprintable()) #False, because of \n, \t

#isspace()- checks if string contains only whitespace, returns True(space, \n, \t, \r) or False
s=" "
print(s.isspace()) #True
s=" \t\n"
print(s.isspace()) #True
s="  A  "
print(s.isspace()) #False, because of A
s=""
print(s.isspace()) #False, because empty string doesn't have any whitespace

#istitle()- returns True(if first character is upper case and others are lower case) or False
s="Amina Kamila Symbat"
print(s.istitle()) #True
s="Amina kamila symbat"
print(s.istitle()) #False
s="AMINA"
print(s.istitle()) #False
s="10 People"
print(s.istitle()) #True, it ignores number, next word should start with an upper case, then others are lower case
s="10 people"
print(s.istitle()) #False, because people started with a lower case
s="A K S"
print(s.istitle()) #True
s="AmIna"
print(s.istitle()) #False, because of I

#isupper()- checks if all characters are upper case, returns True or False(егер ішінде тым болмаса бір кіші әріп болса немесе мәтінде мүлдем әріп болмаса)
s="AMINA"
print(s.isupper()) #True
s="Amina"
print(s.isupper()) #False, all characters should be upper case
s="amina"
print(s.isupper()) #False, all characters should be upper case
s="AMINA 2007"
print(s.isupper()) #True, numbers will be ignored, just all characters from string should be upper case
s="123"
print(s.isupper()) #False, at least 1 upper case shouls be included
s=""
print(s.isupper()) #False