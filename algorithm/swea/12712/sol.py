import sys
sys.stdin = open('input.txt')

T = int(input())
dy1 = [0, 1, 0, -1]     #+모양
dx1 = [1, 0, -1, 0]
dy2 = [1, 1, -1, -1]    #x 모양
dx2 = [1, -1, -1, 1]
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    maxv = 0
    for i in range(N):
        for j in range(N):
            cnt1 = arr[i][j]
            for k in range(4):
                for l in range(1,M):
                    dx = i+dx1[k]*l
                    dy = j+dy1[k]*l
                    if 0<=dx<N and 0<=dy<N:
                        cnt1 += arr[dx][dy]
            if maxv < cnt1:
                maxv = cnt1
    for i in range(N):
        for j in range(N):
            cnt2 = arr[i][j]
            for k in range(4):
                for l in range(1,M):
                    dx = i+dx2[k]*l
                    dy = j+dy2[k]*l
                    if 0<=dx<N and 0<=dy<N:
                        cnt2 += arr[dx][dy]
            if maxv < cnt2:
                maxv = cnt2
    print(f'#{tc} {maxv}')