def fly(s1,s2,s3):
    var = 0
    for i in range(M):
        for j in range(M):
           var += s1[i+s2][j+s3]
    return var

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxv = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            if maxv < fly(arr, i, j):
                maxv = fly(arr, i, j)
    print(f'#{tc} {maxv}')