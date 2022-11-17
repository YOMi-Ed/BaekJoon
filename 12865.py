'''N, K = map(int,input().split())
weight = []
value = []
for _ in range(N) :
    w, v = map(int,input().split())
    weight.append(w)
    value.append(v)
max = 0
for i in range(N) :
    sum = K
    v_m = value[i]
    sum -= weight[i]
    print("11111:  ",weight[i])
    for a in range(i+1,N) :
        if weight[a] <= sum :
            sum -= weight[a]
            v_m += value[a]
            print("a: ",weight[a])
    if max < v_m :
        max = v_m
print(max)'''
import sys

(N, K) = map(int, sys.stdin.readline().split())
item = [[0, 0]]
for i in range(1, N + 1):
    item.append(list(map(int, sys.stdin.readline().split())))
dp = [[0] * (K + 1) for _ in range(N + 1)]    # (N+1) x (K+1) matrix

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= item[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-item[i][0]] + item[i][1])
        else:                
            dp[i][j] = dp[i-1][j]

print(dp)