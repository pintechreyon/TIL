import sys
sys.stdin = open('input.txt')
def bfs(y, x):
    visited[y][x] = 0
    queue = []
    queue.append((y, x))
    while queue:
        cy, cx = queue.pop(0)
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                minus = 0
                if arr[cy][cx] < arr[ny][nx]:
                    minus = arr[ny][nx] - arr[cy][cx]

                if visited[cy][cx] + 1 + minus < visited[ny][nx]:
                    visited[ny][nx] = visited[cy][cx] + 1 + minus
                    queue.append((ny, nx))

    return visited[N-1][N-1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[100000] * N for _ in range(N)]

    print(f'#{tc} {bfs(0, 0)}')