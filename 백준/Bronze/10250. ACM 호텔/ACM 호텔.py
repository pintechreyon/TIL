import sys
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    H, W, N = map(int, sys.stdin.readline().split())
    cnt = 1
    while N > H:
        N -= H
        cnt += 1
    if cnt < 10:
        cnt = '0' + str(cnt)
    print(str(N)+str(cnt))


