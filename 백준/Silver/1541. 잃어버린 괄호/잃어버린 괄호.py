import sys

A = sys.stdin.readline().split("-")

result = 0
arr = []
for i in A:
    num = sum(map(int, i.split("+")))
    arr.append(num)

if len(arr) == 1:
    result = arr[0]
else:
    result = arr[0]
    for i in range(1, len(arr)):
        result -= arr[i]

print(result)