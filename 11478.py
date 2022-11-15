str = input()
com = set()
for i in range(1,len(str)+1) :
    for a in range(len(str)):
        com.add(str[a:a+i])
print(len(com))