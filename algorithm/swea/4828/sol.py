import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    v_min = 0
    v_max = 0
    M = list(map(int, input().split()))
    for i in range(0,N):
        if v_min == 0:
            v_min = M[i]
        elif M[i] < v_min:
            v_min = M[i]

        if v_max == 0:
            v_max = M[i]
        elif M[i] > v_max:
            v_max = M[i]

        result = (v_max - v_min)
    print(f'#{tc} {result}')