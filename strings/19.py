'''
we can't combine strings and numbers like this:
age=36
txt="My name is John, I am "+age
print(txt)
'''
#for that we have format()
age=36
txt=f"My name is John, I am {age}"
print(txt)