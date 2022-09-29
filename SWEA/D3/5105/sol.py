import sys
sys.stdin = open('input.txt')
# 방향 생성자
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x,y):

    # Queue에 x,y좌표와 카운트 추가
    q = [(x, y, -1)]
    while q:
        # Queue에서 꺼내오기
        x, y, c = q.pop(0)
        # 카운트 추가
        c += 1
        # 방향 확인
        for i in range(4):
            # 이미 찾았다면 바로 break
            xx = x + dx[i]
            yy = y + dy[i]
            # 미로 밖을 벗어나는지
            if 0 <= xx < N and 0 <= yy < N:
                # 도착지 찾았으면 카운트 반환
                if arr[xx][yy] == 3: return c
                # 아니면 그 자리 -1로 바꾸고 Queue에 추가
                if arr[xx][yy] == 0: arr[xx][yy] = -1; q.append((xx, yy, c))
    # 도착지를 못찾고 큐를 전부 비웠다면 0 반환
    return 0
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j
    result = bfs(x, y)
    print(f'#{tc} {result}')