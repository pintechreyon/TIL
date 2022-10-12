from collections import deque

T = int(input())
for tc in range(T):
    arr = list(input())
    q = deque()
    for i in arr:
        if i == '(':
            q.append(i)
        else:
            if q and q[-1] == '(':
                q.pop()
            else:
                q.append(i)
    if q:
        print('NO')
    else:
        print('YES')