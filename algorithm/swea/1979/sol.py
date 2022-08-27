import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 0:
                if cnt == M:
                    result += 1
                    cnt = 0
                else:
                    cnt = 0
            else:
                cnt +=1
            if j == N-1:
                if cnt == M:
                    result += 1
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 0:
                if cnt == M:
                    result += 1
                    cnt = 0
                else:
                    cnt = 0
            else:
                cnt += 1
            if j == N-1:
                if cnt == M:
                    result += 1
    print(f'#{tc} {result}')


