import sys
from collections import deque
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    lst = deque()
    cnt = 0
    for n, i in enumerate(arr):
        lst.append([n, i])
    target = lst[M]
    while target in lst:
        if lst[0][1] == max(arr):
            lst.popleft()
            arr.pop(arr.index(max(arr)))
            cnt += 1
        else:
            lst.append(lst[0])
            lst.popleft()
    print(cnt)

