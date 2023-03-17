import sys

N = int(input())

arr = list(map(int, (sys.stdin.readline().split())))

lst = sorted(set(arr))

result = {}
for i, j in enumerate(lst):
    result[j] = i

for k in arr:
    print(result[k], end=' ')
