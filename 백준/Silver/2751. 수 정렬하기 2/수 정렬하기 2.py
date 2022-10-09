import sys
lst = []
N = int(sys.stdin.readline())
for i in range(N):
    lst += [int(sys.stdin.readline())]
lst.sort()
for i in lst:
    print(i, end='\n')