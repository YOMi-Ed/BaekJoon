x, y, w, h = map(int,input().split())

line = [abs(h-y),y,abs(w-x),x] # abs()함수를 쓸 필요는 없을 듯
print(min(line))