import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list_n = set() # 집합을 이용해서....
list_m = set()
for _ in range(N) :
    list_n.add(input())
for _ in range(M) :
    list_m.add(input())
arr = sorted(list(list_n & list_m)) # 교집합을 찾는다
print(len(arr))

for i in arr :
    print(i, end="")