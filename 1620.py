import sys
li1 = {}
li2 = []
N, M = map(int,sys.stdin.readline().split())
for _ in range(N) :
    li1.add(sys.stdin.readline().rstrip())
for _ in range(M) :
    li2.append(sys.stdin.readline().rstrip())
print(li1)
print(li2)
for t in li2 :
    if t.isdigit() == True :
        print(li1[int(t)-1])
    else :
        for i in range(N) :
            if li1[i] == t :
                print(i+1)