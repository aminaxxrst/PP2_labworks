#combining logical operators, precedes: not, and, or
age=25
is_student=False
has_discount_code=True
if (age<18 or age>65) and not is_student or has_discount_code:
    print("Discount applies") #Discount applies
'''
False or False=False
not is_student=True
False and True=False
has_discount_code=True
False or True=True
'''