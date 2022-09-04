import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = []
for i in range(1,N+1):
    arr.append(i)
target = list(map(int, input().split()))
cnt = 0
for i in target:
    for j in range(len(arr)):
        if arr[0] == i:
            arr.pop(0)
            break
        elif len(arr) % 2 == 0:
            if arr.index(i) <= len(arr) // 2 - 1:
                arr.append(arr[0])
                arr.pop(0)
                cnt += 1
            else:
                arr.insert(0, arr[-1])
                arr.pop(-1)
                cnt += 1
        else:
            if arr.index(i) <= len(arr) // 2:
                arr.append(arr[0])
                arr.pop(0)
                cnt += 1
            else:
                arr.insert(0, arr[-1])
                arr.pop(-1)
                cnt += 1
print(cnt)

