import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list_n = set()
list_m = set()
for _ in range(N) :
    list_n.add(input())
for _ in range(M) :
    list_m.add(input())
arr = sorted(list(list_n & list_m))
print(len(arr))

for i in arr :
    print(i, end="")
