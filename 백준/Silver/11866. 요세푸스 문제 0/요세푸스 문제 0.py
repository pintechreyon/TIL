import sys
from collections import deque

N, M = map(int, input().split())
arr = deque(range(1, N+1))
num = M-1
lst = []
while arr:
    for i in range(M-1):
        arr.append(arr.popleft())
    lst.append(str(arr.popleft()))
result = ', '.join(lst)
print(f'<{result}>')