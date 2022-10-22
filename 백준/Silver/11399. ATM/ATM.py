import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
num = 0
result = 0
for i in arr:
    num += i
    result += num
print(result)