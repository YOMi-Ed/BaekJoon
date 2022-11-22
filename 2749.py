# 시간초과가 발생한다.

import sys
input = sys.stdin.readline

fibo = [0,1]
num = int(input())

for i in range(2,num+1) :
    fibo.append(fibo[i-1]+fibo[i-2])
print(fibo[num]%1000000)

# 피사노주기 사용해서 함
N = int(input())
p = 15 * 100000 #Pisano Period
dp = [1] * p
for i in range(3, p):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000
print(dp[N%p])