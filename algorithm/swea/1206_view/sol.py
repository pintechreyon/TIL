import sys
sys.stdin = open("input.txt", "r")
def getValue(pos):
    # 1.pos의 좌측으로 2개, 우측으로 2개 중 가장 큰 값을 구한다.
    maxV = BLD[pos-2]
    if maxV < BLD[pos-1]:
        maxV = BLD[pos - 1]

    if maxV < BLD[pos + 1]:
        maxV = BLD[pos + 1]

    if maxV < BLD[pos + 2]:
        maxV = BLD[pos + 2]

    return maxV
    # 2.pos의 값과 #1에서 구한 값보다 작으면

    #if BLD[pos] < maxV:
         #return 0
    # 3.pos의 값이 #1에서 구한 값보다 크면:
        #return pos의 값 - 1에서 구한값

    #if BLD[pos] > maxV:
        #return BLD[pos] - maxV
# T = int(int(input))
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다
for test_case in range(1, T + 1):
    N = int(input())
    BLD = list(map(int, input().split()))

    cnt = 0
    for i in range(2, N-2):
        if BLD[i] > getValue(i):
            cnt = cnt + BLD[i] - getValue(i)

    print(f'#{test_case} {cnt}')

