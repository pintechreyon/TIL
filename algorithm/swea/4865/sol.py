import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    pat = input()
    target = input()
    maxv = 0
    for i in pat:
        var = 0
        for j in target:
            if i == j:
                var += 1
        if maxv <= var:
            maxv = var
    print(f'#{tc} {maxv}')

