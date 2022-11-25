import sys,math
input = sys.stdin.readline

n = int(input())
matrix = []
for i in range(n) :
    a=list(map(int,input().split()))
    matrix.append(a)
print(matrix)

rst = [[0 for _ in range(n)] for _ in range(n)]
for j in range(1,n) : # j는 가로줄 (1부터 시작하는 이유는 AA는 0이기때문)
    for i in range(j-1, -1, -1) : # i는 세로줄 (j-1을 한 이유는 세로줄은 AA,BB 이런 것 때문에 1칸 앞에서 시작하기 때문) 
        small = math.inf # 최대값을 임의로 줌
        for k in range(i,j) : # i가 줄어들수록 j가 커진다.
            small = min(small, rst[i][k] + rst[k+1][j] + (matrix[i][0] * matrix[k][1] * matrix[j][1])) # rst[i][k]는 가로줄의 숫자가 커지고 rst[k+1][j]는 세로줄의 숫자가 커지기 때문에 k를 붙여줌
            rst[i][j] = small
print(rst[0][n-1])
