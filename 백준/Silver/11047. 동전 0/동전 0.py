import sys
N, M = map(int, sys.stdin.readline().split())
arr = []
cnt = 0
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort(reverse=True)
while M:
    for i in arr:
        if M >= i:
            A = M // i
            cnt += A
            M = M-(i*A)
            break
print(cnt)