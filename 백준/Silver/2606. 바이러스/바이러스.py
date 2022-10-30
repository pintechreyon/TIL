import sys
from collections import deque


def bfs(v):
    visited = [v]
    que = deque([v])
    while que:
        v = que.popleft()
        for i in lst[v]:
            if i not in visited:
                visited.append(i)
                que.append(i)
    return visited


N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]
lst = deque([[] for _ in range(N+1)])
for i in range(M):
    lst[arr[i][0]].append(arr[i][1])
    lst[arr[i][1]].append(arr[i][0])
visited = []
A = len(bfs(1))
print(A-1)
