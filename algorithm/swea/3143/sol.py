import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    target, var = input().split()
    cnt = len(target)
    num = len(target) - len(var)
    i = 0
    while i < len(target):
        if target[i:len(var)+i] == var:
            cnt -= len(var)
            cnt += 1
            i = i+len(var)
        else:
            i+=1
    print(f'#{tc} {cnt}')