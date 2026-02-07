#combining positional-only and keyword-only
def my_function(a, b, /, *, c, d): #a,b-positional while c,d-kwargs
    return a+b+c+d

print(my_function(5, 10, c=15, d=20)) #50