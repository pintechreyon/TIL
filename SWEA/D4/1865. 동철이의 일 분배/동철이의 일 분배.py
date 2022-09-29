# 재귀함수로 해결
def recur(idx, value):
    global answer
    # 백트래킹 조건 (구한 확률이 이미 answer보다 낮으면)
    if answer >= value:
        return
    # 끝까지 골랐는데도 answer < value면
    if idx == N:
        answer = value

    # 모든 열에 대하여, 사용한 적 없는 열이면 재귀함수 실행
    for i in range(N):
        if not used[i]:
            used[i] = True
            recur(idx+1, value * arr[idx][i] / 100)
            used[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    used = [False] * N      # 사용한 열의 정보를 저장할 리스트
    recur(0, 1)             # 확률 100% 부터 시작

    answer *= 100      
    
    print(f'#{tc} {answer:.6f}')