import sys
input = sys.stdin.readline # 시간 복잡도가 낮음 input보다

N, M = map(int,input().split())
li1 = set()
for _ in range(N) :
    li1.add(input())
num = 0
for _ in range(M) : # 이중 for문은 시간복잡도가 크다.
    li2 = input()
    if li2 in li1 :
        num += 1
print(num)