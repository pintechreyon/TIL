import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    num = list(map(int, input().split()))
    N1 = num[0]
    N2 = num[1]
    arr = [list(map(int, input().split())) for _ in range(N1)]
    result = 0
    for i in range(N1 - N2 - 1):
        for j in range(N1 - N2 - 1):
            max_V=0
            for k in range(N2):
                for l in range(N2):
                    max_V += arr[i+k][j+l]
            if result < max_V:
                result = max_V

    print(f'#{tc} {result}')


