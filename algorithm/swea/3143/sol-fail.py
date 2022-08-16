import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    target, var = input().split()
    cnt = len(target)
    num = len(target) - len(var)
    for i in range(num+1):
        if target[i:len(var)+i] == var:
            cnt -= len(var)
            cnt += 1

    print(f'#{tc} {cnt}')


