import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    my_min = 0
    my_max = 0
    arr = list(map(int, input().split()))

    N1 = arr[0]
    N2 = arr[1]

    for i in range(1, N1+1):
        my_min += i
    for i in range(12-N1+1, 12+1):
        my_max += i

    if my_min <= N2 <= my_max:
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')
