import sys
sys.stdin = open('input.txt')
N, M = map(int, input().split())
arr = list(range(1, N+1))
var = 0
result = []
for i in range(N):
    var += M-1
    if var >= len(arr):
        var = var % len(arr)
    result.append(str(arr.pop(var)))

print(f'<{", ".join(result)}>')
