import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result90 = [[0]*N for _ in range(N)]
    result180 = [[0]*N for _ in range(N)]
    result270 = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            result90[i][j] = arr[N-1-j][i]

    arr = result90
    for i in range(N):
        for j in range(N):
            result180[i][j] = arr[N-1-j][i]

    arr = result180
    for i in range(N):
        for j in range(N):
            result270[i][j] = arr[N-1-j][i]

    print(f'#{tc}')
    for i in range(N):
        print(''.join(map(str, result90[i])), end = ' ')
        print(''.join(map(str, result180[i])), end = ' ')
        print(''.join(map(str, result270[i])))