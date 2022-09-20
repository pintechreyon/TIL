import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = float(input())  # 소수를 받기 위해 타입을 float로 받는다
    cnt = 1  # 2의 지수를 올리기 위해 사용
    binary = []  # 이진수로 변환하는 값을 담기위한 리스트
    while N != 0:  # N이 0이되면 연산을 종료시킨다
        if N >= 2 ** -cnt:  # N이 2의 -cnt승 보다 커야 뺄 수 있고 이때 이진수에 1을 추가한다
            N = N - (2 ** -cnt)
            binary.append('1')
            cnt += 1
        else:  # N이 2의 -cnt승 보다 작다면 빼지 않고 지수를 올려서 다음 순서에 뺀다
            binary.append('0')
            cnt += 1
        if len(binary) > 12:  # 조건 상 12자리가 넘을 시 'overflow'로 나오게 해야하므로 그 이상 연산을 하지 않는다
            break
    if len(binary) > 12:
        print(f'#{tc} overflow')
    else:
        print(f"#{tc} {''.join(binary)}")
