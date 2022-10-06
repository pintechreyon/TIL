import sys
N = int(sys.stdin.readline().rstrip())
lst = []
result = []
for i in range(N):
    lst.append(sys.stdin.readline().rstrip())
lst = list(set(lst))
lst.sort()
lst.sort(key=len)
for i in lst:
    print(i)