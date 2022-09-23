import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    D, M, M3, Y = map(int, input().split())
    arr = list(map(int, input().split()))
    D_M = []
    L = 0
    for i in range(12):
        if[i] != 0:
            L += 1
    for i in arr:
        if i*D < M:
            D_M.append(i*D)
        else:
            D_M.append(M)
    M_1 = [0]*12
    for i in range(12):
        if D_M[i] != 0:
            if M < D_M[i] + D_M[i+1] + D_M[i+2]:
                D_M[i] = M
                D_M[i + 1] = D_M[i + 2] = 0






