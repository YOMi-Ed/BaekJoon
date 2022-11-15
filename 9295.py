num = int(input())
case = {}
for i in range(num) :
    num1, num2 = map(int,input().split())
    case[i+1] = num1+num2
for i in range(num) :
    print("Case "+ str(i+1) +": "+ str(case[i+1]))