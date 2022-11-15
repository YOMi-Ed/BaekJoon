X1, Y1 = map(int,input().split())
X2, Y2 = map(int,input().split())
X3, Y3 = map(int,input().split())

if X1 == X2 :
    print(X3, end=" ")
    if Y1 == Y2 :
        print(Y3)
    elif Y1 == Y3 :
        print(Y2)
    elif Y2 == Y3 :
        print(Y1)
elif X1 == X3 :
    print(X2, end=" ")
    if Y1 == Y2 :
        print(Y3)
    elif Y1 == Y3 :
        print(Y2)
    elif Y2 == Y3 :
        print(Y1)
elif X2 == X3 :
    print(X1, end=" ")
    if Y1 == Y2 :
        print(Y3)
    elif Y1 == Y3 :
        print(Y2)
    elif Y2 == Y3 :
        print(Y1)