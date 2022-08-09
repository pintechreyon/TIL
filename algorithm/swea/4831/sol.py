import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    can_go, last, charger = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    #c_list[i] + can_go < c_list[i+1}이면 0으로 환산
    for i in range(charger):
        if i < range(charger)[-1]:
            if c_list[i+1] > can_go + c_list[i]:
                result = 0
                break
        else:
            result = int((last - c_list[0]) / can_go)
            break
        if c_list[-1] + can_go < last:
            result = 0

    print(f'#{tc} {result}')