import sys
sys.stdin = open('input.txt')

T = int(input())
def my_abs(s1):
    if s1 >= 0:
        return s1
    else:
        return -s1
for tc in range(1, T+1):
    N = int(input())
    L1 = list(map(int, input().split()))
    L2 = list(map(int, input().split()))
    L3 = list(map(int, input().split()))
    L4 = list(map(int, input().split()))
    L5 = list(map(int, input().split()))
    cnt = 0
    for i in range(5):
        if i < 4:
            num = my_abs(L1[i] - L2[i])*2 + my_abs(L1[i] - L1[i+1])*2
            cnt += num
        elif i == 4:
            num = my_abs(L1[i] - L2[i]) * 2
            cnt += num
    for i in range(5):
        if i < 4:
            num = my_abs(L2[i] - L3[i])*2 + my_abs(L2[i] - L2[i+1])*2
            cnt += num
        elif i == 4:
            num = my_abs(L2[i] - L3[i]) * 2
            cnt += num
    for i in range(5):
        if i < 4:
            num = my_abs(L3[i] - L4[i])*2 + my_abs(L3[i] - L3[i+1])*2
            cnt += num
        elif i == 4:
            num = my_abs(L3[i] - L4[i]) * 2
            cnt += num
    for i in range(5):
        if i < 4:
            num = my_abs(L4[i] - L5[i])*2 + my_abs(L4[i] - L4[i+1])*2
            cnt += num
        elif i == 4:
            num = my_abs(L4[i] - L5[i]) * 2
            cnt += num
    for i in range(5):
        if i < 4:
            num = my_abs(L5[i] - L5[i+1])*2
            cnt += num
    print(cnt)
