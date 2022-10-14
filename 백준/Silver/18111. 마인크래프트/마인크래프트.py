import sys
input = sys.stdin.readline
count, height = -1, 0

n, m, b = map(int, input().split())
land = []
for _ in range(n):
    land.extend(list(map(int, input().split())))
land.sort(reverse=True)

for h in range(land[-1], land[0]+1):   
    c, tmp = 0, b
    for l in land:                     
        if l > h:   
            c += (l-h)*2
            tmp += l-h
        elif l < h: 
            c += h-l
            tmp -= h-l
    
    if tmp < 0:
        break

    if count == -1 or c <= count:
        count = c
        height = h


print(count, height)