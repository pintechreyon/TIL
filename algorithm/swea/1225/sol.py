import sys
sys.stdin = open('input.txt')


for tc in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))
    var = 0
    for i in arr:
        if var < i:
            var = i
    while arr[-1] > 0:
        for i in range(1, 6):
            if arr[0] <= i:
                arr.append(0)
                arr.pop(0)
                break
            else:
                arr.append(arr[0] - i)
                arr.pop(0)
    print(f"#{tc} ",end = '')
    print(*arr)





