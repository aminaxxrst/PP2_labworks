#else- run a block of code once when the condition no longer is true
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")
#1 2 3 4 5 i is no longer less than 6