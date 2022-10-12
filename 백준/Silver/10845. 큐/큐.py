import sys
from collections import deque
N = int(input())
q = deque()
for i in range(N):
    A = list(sys.stdin.readline().split())
    if len(A) == 2:
        q.append(A[1])
    else:
        if A == ['pop']:
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif A == ['size']:
            print(len(q))
        elif A == ['empty']:
            if q:
                print(0)
            else:
                print(1)
        elif A == ['front']:
            if q:
                print(q[0])
            else:
                print(-1)
        else:
            if q:
                print(q[-1])
            else:
                print(-1)