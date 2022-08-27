import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    up = 0
    var = 0
    arr = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        if  i <= N//2:
            for j in arr[i][N//2 - up:N//2 + 1 + up]:
                var += j
            up += 1
        elif i > N // 2:
            up -= 1
            for j in arr[i][N // 2 + 1 - up:N // 2 + up]:
                var += j
    print(f'#{tc} {var}')

