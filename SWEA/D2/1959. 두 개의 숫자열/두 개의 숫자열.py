T = int(input())
for tc in range(1,T+1):
    N, M = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    result = 0
    if N < M:
        for i in range(M - N + 1):
            maxv = 0
            for j in range(len(A)):
                maxv += A[j]*B[j]
            A = [0] + A
            if result < maxv:
                result = maxv
    if N == M:
        for j in range(len(A)):
            result += A[j] * B[j]
    if M < N:
        for i in range(N - M + 1):
            maxv = 0
            for j in range(len(B)):
                maxv += A[j]*B[j]
            B = [0] + B
            if result < maxv:
                result = maxv
        
    print(f'#{tc} {result}')