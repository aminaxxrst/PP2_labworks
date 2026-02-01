#else- block will not be executed if the loop is stopped by a break statement
for x in range(6):
    if x==3: break
    print(x)
else:
    print("Finally finished!")
#0 1 2