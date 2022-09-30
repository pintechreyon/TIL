arr = list(map(int, input().split()))
result = 0
for i in range(5):
    result += arr[i]**2
result = result % 10
print(result)