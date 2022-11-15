import sys
input = sys.stdin.readline
li1 = {} # 딕셔너리로 만듬
N, M = map(int,input().split())
for i in range(N) :
    tt = input().rstrip() #rstrip 인자로 전달된 문자를 String 오른쪽에서 제거한다.
    li1[i+1] = tt
    li1[tt] = i+1
for _ in range(M): 
    quiz = input().rstrip()
    if quiz.isdigit() == True : #isdigit 숫자인지 확인해주는 함수
        print(li1[int(quiz)])
    else :
        print(li1[quiz])