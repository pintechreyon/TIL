import sys
sys.stdin = open('input.txt')

def fact(s1):
    if s1 > 1:
        return s1 * (fact(s1-1))
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = fact(M) // (fact(M-N) * fact(N))
    print(result)