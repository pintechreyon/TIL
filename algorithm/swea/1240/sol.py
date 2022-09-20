import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 받기

for tc in range(1, T+1):
    N, M = map(int, input().split())  # 세로 가로 길이 받기
    arr = [input() for _ in range(N)]  # 패턴 비교를 위해 문자열로 받기
    target = []  # 0으로 반복되는 줄을 제외하고 비교대상을 넣는 리스트
    result = 0
    flag = False  # 반복문 탈출용
    pattern = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001',
               '0101111', '0111011', '0110111', '0001011']  # 0~9까지 일치하는 암호를 숫자로 변환하기 위해 인덱스를 맞춤
    for i in arr:  # 0만 반복되는 줄은 제거
        if i == '0' * M:
            continue
        else:
            target = i  # 0외에 값이 들어가는 줄을 추출
            break
    for i in range(M-56):  # 암호문이 56자 이므로 전체길이에서 56을 뺀만큼 반복문을 돌림
        if flag:
            break
        num = []  # 변환한 암호를 저장하기 위한 리스트
        for j in range(i, i+56, 7):  # 첫번째 인덱스 부터 56줄씩 조건에 맞는지 확인
            if target[j:j+7] not in pattern:  # 조건에 맞지 않는 줄이 있을 시 다음 순서로 넘어감
                result = 0
                break
            else:
                num.append(pattern.index(target[j:j+7]))  # 조건에 맞을 시 num 리스트에 추가
        if len(num) == 8:  # num 리스트에 암호 8개가 전부 들어왔을 때
            for k in range(8):  # 홀수 숫자는 3을 곱해서 더하고 짝수는 그대로 더해서 10의 배수라면 암호의 합을 저장하고 반복문 탈출
                if k % 2 == 0:
                    result += num[k]*3
                else:
                    result += num[k]
            if result % 10 == 0:
                flag = True
                result = sum(num)

    print(f'#{tc} {result}')
