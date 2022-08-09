import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = list(map(int, input().split()))
    N1, N2 = N[0], N[1]
    M = list(map(int, input().split()))
    v_max = 0
    v_min = 0
    for i in range(N1-N2+1):
        now = 0
        for l in range(i, i+N2):
            now += M[i]
        if v_min > now or v_min == 0:
            v_min = now
        if v_max < now:
            v_max = now

    print(f'#{tc} {v_max-v_min}')
