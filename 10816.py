import sys
from collections import Counter
''' 6 3 2 10 10 10 -10 -10 7 3 이걸 Counter하면 
{10: 3, 3: 2, -10: 2, 6: 1, 2: 1, 7: 1} 이렇게 바뀐다.'''
input = sys.stdin.readline

M = int(input())
list_m = list(map(int,input().split()))

N = int(input())
list_n = list(map(int,input().split()))

list_m = Counter(list_m)
print(list_m)

for i in list_n :
    print(list_m[i], end=" ")

    
#시간 초과 발생 코드
'''
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

M = int(input())
list_m = sorted(list(map(int,input().split())))

N = int(input())
list_n = list(map(int,input().split()))

for i in list_n :
    if i in list_m :
        print(bisect_right(list_m,i)-bisect_left(list_m,i), end=" ")
    else :
        print(0,end=" ")'''