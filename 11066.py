# 이 방법도 좋은데 이해 하기 어려움
import sys
input = sys.stdin.readline
MAX = sys.maxsize

t = int(input())

def solve() :
    n = int(input())
    file = list(map(int, input().split()))
    dp = [[0] * n for _ in range(n)]
    print(dp)
    sum = [0]
    for f in file :
        sum.append(sum[-1]+f)
    print("sum : "  + str(sum))
    for d in range(1,n) :
        print("d :" +str(d))
        for i in range(n-d) :
            print("i :" +str(i))
            j = d+i
            print("j :" +str(j))
            dp[i][j] = MAX
            print(dp[i][j])
            for k in range(i,j) :
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+sum[j+1]-sum[i])
                print("dp[i][j]: " +str(dp[i][j]))
    print(dp[0][n-1])
for i in range(t) :
    solve()

# 45-46줄부분이 이게 더 이해하기 쉬움
import sys, math
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    rst = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(1,n) : # j는 가로줄 (1부터 시작하는 이유는 AA는 0이기때문)
        for i in range(j-1, -1, -1) : # i는 세로줄 (j-1을 한 이유는 세로줄은 AA,BB 이런 것 때문에 1칸 앞에서 시작하기 때문) 
            small = math.inf # 최대값을 임의로 줌
            for k in range(i,j) : # i가 줄어들수록 j가 커진다.
                small = min(small, rst[i][k] + rst[k+1][j]) # rst[i][k]는 가로줄의 숫자가 커지고 rst[k+1][j]는 세로줄의 숫자가 커지기 때문에 k를 붙여줌
            rst[i][j] = small +sum(arr[i:j+1]) # 마지막에 더해줘야 최소 값이 구해짐
    print(rst[0][n-1])
t =int(input())
for _ in range(t) :
    solve()