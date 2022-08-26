import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        j = 0
        row = 0
        col = 0
        while j < N:
            if arr[i][j] != 0:
                row += 1
            elif
