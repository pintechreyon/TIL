import sys
N = int(sys.stdin.readline())
arr = []
stack = []
result = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
for i in range(1, N+1):
    stack.append(i)
    result.append('+')
    while stack and stack[-1] == arr[0]:
        stack.pop()
        arr.pop(0)
        result.append('-')
if arr:
    print('NO')
else:
    print(*result, sep="\n")

