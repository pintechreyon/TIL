import sys
N = int(input())
arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
cnt = 0
num = 0
for x, y in arr:
    if x >= num:
        num = y
        cnt += 1
print(cnt)
