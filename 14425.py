import sys
input = sys.stdin.readline

N, M = map(int,input().split())
li1 = set()
li2 = []
for _ in range(N) :
    li1.add(input())
for _ in range(M) :
    li2.append(input())
num = 0
for st1 in li1 :
    for st2 in li2 :
        if st1 == st2 :
            num += 1
print(num)