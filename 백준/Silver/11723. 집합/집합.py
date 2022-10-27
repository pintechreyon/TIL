import sys

N = int(input())
lst = []
for i in range(N):
    A = list(sys.stdin.readline().split())
    if len(A) == 2:
        if A[0] == 'add' and int(A[1]) not in lst:
            lst.append(int(A[1]))
        elif A[0] == 'remove' and int(A[1]) in lst:
            lst.pop(lst.index(int(A[1])))
        elif A[0] == 'check':
            if int(A[1]) in lst:
                print(1)
            else:
                print(0)
        elif A[0] == 'toggle':
            if int(A[1]) in lst:
                lst.pop(lst.index(int(A[1])))
            else:
                lst.append(int(A[1]))
    else:
        if A[0] == 'all':
            lst = list(range(1, 21))
        else:
            lst = []
