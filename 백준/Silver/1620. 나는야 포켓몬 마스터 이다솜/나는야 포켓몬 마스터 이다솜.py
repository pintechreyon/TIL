import sys
N, M = map(int, sys.stdin.readline().split())
lst = {}
for i in range(N):
    A = sys.stdin.readline().rstrip()
    lst[str(i+1)] = A
    lst[A] = i+1
for i in range(M):
    A = sys.stdin.readline().rstrip()
    print(lst[A])