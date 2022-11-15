sang = int(input())
s_l =set(map(int,input().split()))
card = int(input())
c_l = list(map(int,input().split()))

for i in c_l :
    if i in s_l :
        print(1, end=" ")
    else :
        print(0, end=" ")