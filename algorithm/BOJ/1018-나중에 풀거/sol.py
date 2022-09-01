import sys
sys.stdin = open('input')

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N-8):
    for j in range(M-8):
        var = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if arr[k][l] == arr[i][j]:


