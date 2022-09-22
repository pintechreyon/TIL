import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])
    answer = 0
    end = 0
    for s, e in arr:
        if end <= s:
            answer += 1
            end = e
    print(f'#{tc} {answer}')