import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]  # 10x10의 빈 리스트 생성
    result = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1): #입력된 범위에 대하여 색칠 진행
                if arr[i][j] != color:
                    arr[i][j] += color
                if arr[i][j] == 3: #색칠 후 그곳이 값이 3이면(보라색이면) 결과값 + 1
                    result += 1

    print(f'#{tc} {result}')
