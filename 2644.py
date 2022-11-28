# 엉망인 내 코드... 아무리해도 더 고치지 못하겠다...
people = int(input())
chon1, chon2 = map(int,input().split())
rel = int(input())
rel_list = [[]]
for _ in range(people) :
    rel_list.append([])
for _ in range(rel) :
    a, b = map(int,input().split())
    rel_list[a].append(b)
    rel_list[b].append(a)
print(rel_list)
visited = [False] * (people+1)
count = [chon1]
def dfs(rel_list, start, visited) :
    visited[start] = True
    for i in range(len(rel_list[start])) :
        print("start" + str(start))
        print(i)
        print(count)
        if rel_list[start][i] in count and visited[start] == True:
            for a in range(len(count)-1,0,-1) :
                print("a : " +str(a))
                if count[a-1] == rel_list[start][i] :
                    break
                count.pop()
        count.append(rel_list[start][i])
        if chon2 == count[-1] :
            print("2222  " +str(len(count)-1))
            return len(count)-1
        if not visited[rel_list[start][i]] :
            dfs(rel_list, rel_list[start][i], visited)
dfs(rel_list, chon1, visited)
print("count1111 " + str(count))

if chon2 not in count :
    print(-1)

from collections import deque
node = int(input())
a, b = map(int, input().split())
num = int(input())
graph = [[]*node for _ in range(node+1)]
for _ in range(num):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

visited = [False]*(node+1)
visited[a] = True  # 촌수를 계산해야하는 사람 중 한명의 시작점을 true로
dq = deque([a])
cnt = [False]*(node+1)

# for i in graph[a]:
#     dq.append(i)
while(dq): # while문 생각을 어캐 하는거지... a 기준으로 모든 촌 수를 구한다.
    k = dq.popleft()
    for i in graph[k]:
        if visited[i] == False:
            dq.append(i)
            cnt[i] = cnt[k]+1
            visited[i] = True
if cnt[b] > 0:
    print(cnt[b])
else:
    print(-1)

