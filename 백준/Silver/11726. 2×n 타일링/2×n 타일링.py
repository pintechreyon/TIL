N = int(input())
if N < 3:
    arr = [0] * 3
    arr[1] = 1
    arr[2] = 2
else:
    arr = [0] * (N + 1)
    arr[1] = 1
    arr[2] = 2
    for i in range(3, N+1):
        arr[i] = arr[i-1] + arr[i-2]
print(arr[N] % 10007)