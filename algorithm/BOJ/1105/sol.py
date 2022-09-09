import sys
sys.stdin = open('input.txt')

N, M = input().split()
result = 0
if len(N) == len(M):
    for i in range(len(N)):
        if N[i] == '8' and M[i] == '8':
            result += 1
        elif N[i] == M[i]:
            continue
        else:
            break
print(result)
