import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    start = 0
    result = 0
    while True:
        if start + arr[start] >= N-1:
            break
        var = 0
        for i in range(start+arr[start], start, -1):
            if i + arr[i] > var:
                var = i + arr[i]
                start = i
        result += 1
    print(f'#{tc} {result}')


