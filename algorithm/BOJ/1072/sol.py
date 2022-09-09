import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

Z = M * 100 // N
if Z >= 99:
    cnt = -1
else:
    cnt = 0
    start = 1
    end = 1000000000
    # 승률 계산해주기 !!  // vs int( a / b) 의 차이점 파악해두기(부동소수점 오류)
    while start <= end:
        mid = (start + end) // 2
        if (M + mid) * 100 // (N + mid) > Z:
            cnt = mid
            end = mid - 1
        else:
            start = mid + 1
print(cnt)