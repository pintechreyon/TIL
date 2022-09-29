N = int(input())
arr = list(map(int, input().split()))
max_num = max(arr)
var = 0
for i in arr:
    var += i / max_num * 100
result = var / N
print(result)