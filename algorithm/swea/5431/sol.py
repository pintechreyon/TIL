import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    result = []
    for i in range(1,N+1):
        if i not in arr:
            result.append(i)
    print(f'#{tc} ',end = '')
    print(*result)
