import sys
sys.stdin = open('input.txt')
T = int(input())
for TC in range(1, T+1):
    P, A, B = map(int, input().split())
    cnt_A = 0
    cnt_B = 0
    l = 1
    r = P
    while 1:
        c = int((l+r)/2)
        cnt_A += 1
        if c == A:
            break
        elif c <= A:
            l = c
        else:
            r = c
    l = 1
    r = P
    while 1:
        c = int((l+r)/2)
        cnt_B += 1
        if c == B:
            break
        elif c <= B:
            l = c
        else:
            r = c

    if cnt_A == cnt_B:
        print("#%d %d" %(TC, 0))
    elif cnt_A > cnt_B:
        print("#%d %c" %(TC, 'B'))
    else:
        print("#%d %c" %(TC, 'A'))