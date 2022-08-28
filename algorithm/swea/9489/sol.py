T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        cnt_r = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt_r += 1
                if result < cnt_r:
                    result = cnt_r
            else:
                cnt_r = 0

    for i in range(M):
        cnt_c = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt_c += 1
                if result < cnt_c:
                    result = cnt_c
            else:
                cnt_c = 0
    print(f'#{tc} {result}')