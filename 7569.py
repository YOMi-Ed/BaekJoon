from collections import deque
q = deque()
M, N, H = map(int,input().split())

tomato = [[] for i in range(H)]
day = 0
zero = 0
move = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
for a in range(H) :
    for _ in range(N) :
        tomato[a].append(list(map(int,input().split())))

def change (q) :
    global day
    cpy = q[-1]
    while q :
        rr = q.popleft()
        for i in range(6) :
            dz = rr[0] + move[i][0]
            dy = rr[1] + move[i][1]
            dx = rr[2] + move[i][2]
            if 0 <= dz < H and 0 <= dy < N and 0 <= dx < M and tomato[dz][dy][dx] == 0 :
                tomato[dz][dy][dx] = 1
                q.append([dz,dy,dx])
        if rr == cpy and q:
            day += 1
            cpy.clear()
            if q :
                cpy = q[-1]

for a in range(H) :
    for b in range(N) :
        for c in range(M) :
            if tomato[a][b][c] == 0 :
                zero += 1
            if tomato[a][b][c] == 1 :
                q.append([a,b,c])
if q :
    change(q)

cnt = 0
for a in range(H) :
    for b in range(N) :
        for c in range(M) :
            if tomato[a][b][c] == 0 :
                cnt += 1
            
if zero == 0 :
    print(0)
elif cnt > 0 :
    print(-1)
else :
    print(day)