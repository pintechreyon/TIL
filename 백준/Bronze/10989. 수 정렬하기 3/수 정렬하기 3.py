import sys
N = int(sys.stdin.readline())
arr = [0]*10001
for i in range(N):
    arr[int(sys.stdin.readline())] += 1
for i in range(10001):
    for j in range(arr[i]):
        if arr[i] != 0:
            print(i, end='\n')