import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    go, last, charge = list(map(int, input().split()))
    c_list = list(map(int, input().split()))

    cnt = 0
    pos = 0
    run = 0+go
    station = [0]*last
    for i in c_list:
        station[i] += 1

    while run < last:
        if pos == run:
            cnt = 0
            break
        elif station[run] == 1:
            pos = run
            run = pos + go
            cnt += 1
        else:
            run -= 1
    print(f'#{tc} {cnt}')
        