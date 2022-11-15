ans = []
while(1) :
    li = list(map(int,input().split()))
    if li[0] == 0 and li[1] == 0 and li[2] == 0 :
        break
    if li[2]*li[2] == (li[0]*li[0]) + (li[1]*li[1]) :
        ans.append("right")
    else :
        ans.append("wrong")
    li.clear()
for i in ans :
    print(i)