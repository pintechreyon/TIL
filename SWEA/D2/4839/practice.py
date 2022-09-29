import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    result = []
    cnt = 0
    for i in A, B:
        l = 1
        r = P
        c = 0
        while True:
            if c == i:
                break
            c = int((l+r)/2)
            if c < i:
                l = c
            else:
                r = c
            cnt += 1
        result.append(cnt)
    print(result)

