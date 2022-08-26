import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    H = M
    result = ''
    flag = False
    while arr:
        for i in range(len(arr)):
            if arr[i] < M:
                result = "Impossible"
                flag = True
                break
        if flag == True:
            break
        if len(arr) <= K:
            result = "Possible"
            break
        else:
            M = M + H
            #del arr[:K]
            arr = arr[K:]

    print(f'#{tc} {result}')

