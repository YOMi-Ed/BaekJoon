
# 아무래도 내 방법은 구현이 힘들...
'''
num = int(input())
ground = []
height = 0
h_n = 0
width = 0
w_n = 0

for i in range(6) :
    ground.append(list(map(int,input().split())))
    if ground[i][0] == 3 or ground[i][0] == 4 : # 북, 남
        if height < ground[i][1] :
            height = ground[i][1]
            h_n = ground[i]
    elif ground[i][0] == 1 or ground[i][0] == 2 : # 동, 서
        if width < ground[i][1] :
            width = ground[i][1]
            w_n = ground[i]
ent = width * height
print(ent)
if (ground.index(h_n) == 0 and ground.index(w_n) == 1) or (ground.index(h_n) == 1 and ground.index(w_n) == 0) :
    0
else :
    ground[0]

print(ground.index(h_n))
ground.remove(h_n)
ground.remove(w_n)
print(ground)
minus = ground[1][1] * ground[2][1]
print((ent-minus) * num)
'''
melon = int(input())

direction = []
distance = []

for _ in range(6):
    dir, dis = map(int, input().split())
    direction.append(dir)
    distance.append(dis)

direction += direction
distance += distance
print(direction)
print(distance)

idx = 0
for i in range(10):
    if direction[i] == direction[i+2] and direction[i+1] == direction[i+3]:
        idx = i
        break

area = (distance[idx+4] * distance[idx+5]) - (distance[idx+1] * distance[idx+2])
print(area*melon)
