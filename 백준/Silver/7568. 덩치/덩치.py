import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lst = []
for i in range(len(arr)):
    cnt = 1
    for j in range(len(arr)):
        if i != j:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                cnt += 1
    lst.append(cnt)
print(*lst)