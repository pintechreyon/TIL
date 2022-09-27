import sys
sys.stdin = open('input.txt')

def DFS(idx, total):
    global max_v
    if idx == N:
        if total > max_v:
            max_v = total
        return

    for i in range(N):
        if arr[idx][i] == 0:
            return
        if i not in visited:
            if total == 0:
                visited.append(i)
                DFS(idx + 1, arr[idx][i])
                visited.pop()
            else:
                visited.append(i)
                DFS(idx+1, total*arr[idx][i])
                visited.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / (10 ** 2)
    visited = []
    max_v = 0
    DFS(0, 0)
    max_v = max_v*100
    print(f'#{tc} {max_v:.6f}')