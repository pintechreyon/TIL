N, M = map(int, input().split())
if M < 45:
    N -= 1; M += 15
else:
    M -= 45
if N < 0:
    N = 23
print(f'{N} {M}')