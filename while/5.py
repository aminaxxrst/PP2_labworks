#else- will not be executed if the loop is stopped by a break statement
i=1
while i<6:
    print(i)
    if i==3: break
    i+=1
else:
    print("i is no longer less than 6")
#1 2 3