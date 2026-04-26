#zfill(number)- zero fill, бос орындарды 0 мен толтыру
s="Amina"
print(s.zfill(10)) #"00000Amina"
print(s.zfill(2)) #"Amina"
s="-42"
print(s.zfill(5)) #"-0042"
print(s.rjust(5, '0')) #"00-42"