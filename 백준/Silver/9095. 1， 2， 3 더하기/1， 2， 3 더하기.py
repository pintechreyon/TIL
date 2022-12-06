arr = [0] * 11
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4, 11):
    arr[i] = sum(arr[i-3:i])
T = int(input())
for tc in range(T):
    print(arr[int(input())])