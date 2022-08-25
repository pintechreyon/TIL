import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    S, G = map(int,input().split())
    cnt = 0
    result = 0
    Q = [S]
    while result == 0 and cnt < M+1:
        lst = []
        cnt += 1

        for i in Q:
            for j in arr:
                if j[1] not in lst and i == j[0]:
                    lst.append(j[1])
                elif j[0] not in lst and i == j[1]:
                    lst.append(j[0])

                if lst and lst[-1] == G:
                    result = cnt
                    break
            if result:
                break
        Q = lst

    print(f'#{tc} {result}')