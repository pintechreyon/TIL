import sys
sys.stdin = open('input.txt')

def DFS(idx, total):
    global min_v
    if idx == N:
        if total < min_v:
            min_v = total
        return
    if total > min_v:
        return

    for i in range(N):
        if i not in visited:
            visited.append(i)
            DFS(idx+1, total+arr[idx][i])
            visited.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = list(zip(arr))
    print(A)
    # visited = []
    # min_v = 100
    # DFS(0, 0)
    # print(f'#{tc} {min_v}')
