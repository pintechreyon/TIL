import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    num = M % N
    arr = list(map(int, input().split()))
    for i in range(num):
        arr.append(arr[0])
        arr.pop(0)
    print(f'#{tc} {arr[0]}')


