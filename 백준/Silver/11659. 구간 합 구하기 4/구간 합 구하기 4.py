import sys
n, k = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))
dap = [0]
for i in range(n):
    dap.append(dap[i] + x[i])
for t in range(k):
    a, b = map(int, sys.stdin.readline().split())
    print(dap[b]-dap[a-1])