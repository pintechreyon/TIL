import sys
sys.stdin = open('input.txt')

T = 10
N = 100
for tc in range(1, T+1):
    no = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    garo = 0
    sero = 0
    L_dagag = 0
    R_dagag = 0
    for i in range(N):
        maxA = 0
        maxB = 0
        L_dagag += arr[i][i]
        R_dagag += arr[i][N-1-i]
        for j in range(N):
            maxA += arr[i][j]
            maxB += arr[j][i]
        if maxA > garo:
            garo = maxA
        if maxB > sero:
            sero = maxB

    for i in [garo, sero, R_dagag, L_dagag]:
        if result < i:
            result = i
    print(f'#{tc} {result}')