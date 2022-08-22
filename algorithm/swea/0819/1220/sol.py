import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    cnt = 0
    for i in range(N):
        j = 0
        while j < N:
            if arr[j][i] == 1:
                k = j + 1
                while k < N:
                    if arr[k][i] == 2:
                        cnt += 1
                        break
                    else:
                        k += 1
                j = k + 1
            else:
                j += 1
    print(f'{tc} {cnt}')
