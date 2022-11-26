import sys

input = sys.stdin.readline
people, game = input().split()

player = []

for _ in range(int(people)) :
    player.append(input())

player = set(player) # 집합은 중복을 줄여줘서 좀 더 빠르게 작동함.

if game == 'Y' :
    print(len(player)) 
elif game == 'F' :
    print(len(player)//2)
elif game == 'O' :
    print(len(player)//3)