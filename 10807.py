num = int(input())
num_li = list(map(int, input().split()))
search = int(input())
number = 0
for i in num_li :
    if i == search :
        number += 1
print(number)