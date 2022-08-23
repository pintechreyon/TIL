import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    dump = int(input())
    arr = list(map(int, input().split()))
    for i in range(dump):
        for j in range(len(arr)):
            if arr[j] == min(arr):
                arr[j] = arr[j]+1
                break

    for i in range(dump):
        for j in range(len(arr)):
            if arr[j] == max(arr):
                arr[j] = arr[j]-1
                break
    result = max(arr)-min(arr)
    print(f'#{tc} {result}')
