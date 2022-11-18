'''num = int(input())
 
bro_li = []
baek_li = []
for _ in range(num) :
    i = int(input())
    baek_li.append(i)
    baek_li = sorted(baek_li)
    if len(baek_li) % 2 == 1 :
        tt = int(len(baek_li) / 2)
        bro_li.append(baek_li[tt])
    else :
        tt = int(len(baek_li) / 2)
        bro_li.append(baek_li[tt-1])
for a in bro_li :
    print(a)'''
'''import sys
input = sys.stdin.readline

num = int(input())
max_Heap = []
min_Heap = []
store = []
for _ in range(num) :
    number = int(input())
    if len(max_Heap) == len(min_Heap) :
        max_Heap.append(number)
    else :
        min_Heap.append(number)   
    if len(min_Heap) > 0 :
        if max_Heap[-1] > min_Heap[0] :
            a = max_Heap[-1]
            b = min_Heap[0]
            max_Heap[-1] = b
            min_Heap[0] = a
    max_Heap = sorted(max_Heap)
    store.append(max_Heap[-1])
for i in store :
    print(i)'''

import sys, heapq

leftHeap=[]
rightHeap=[]
n = int(sys.stdin.readline())
for i in range(n):
    s = int(sys.stdin.readline())
    
    if len(leftHeap) == len(rightHeap): # 왼쪽에서 부터 값을 집어 넣음
        heapq.heappush(leftHeap, -s) # 왼쪽 힙에 값 저장
    else:
        heapq.heappush(rightHeap, s) # 오른쪽 힙에 값 저장
    print("leftHeap: "+ str(leftHeap) + "rightHeap: "+ str(rightHeap))

    
    # 오른쪽 힙에 값이 들어 있으면서 오른쪽 힙의 최솟값보다 왼쪽힙의 최대값이 더 큰 경우
    # 서로 값을 바꿔줌
    if rightHeap and rightHeap[0] < -leftHeap[0]: 
        t1 = heapq.heappop(leftHeap)
        t2 = heapq.heappop(rightHeap)
        
        heapq.heappush(leftHeap, -t2)
        heapq.heappush(rightHeap, -t1)
    print(-leftHeap[0]) # 왼쪽 힙의 제일 큰 값이 중간값이므로 출력
print(list(leftHeap), list(rightHeap))

