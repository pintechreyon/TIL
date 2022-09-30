N = int(input())
arr = input()
result = 0
for i in range(N):
    result += (ord(arr[i])-96) * (31**i)
print(result % 1234567891)