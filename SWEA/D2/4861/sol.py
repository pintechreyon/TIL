import sys
sys.stdin = open('input.txt')


def palindrome(s1):
    r_s1 = list(zip(*s1))
    r_result = ''
    for i in range(N):
        for j in range(N - M + 1):
            if s1[i][j:j + M] == s1[i][j:j + M][::-1]:
                print(f'#{tc} {s1[i][j:j + M]}')
                return ()
    for i in range(N):
        for j in range(N - M + 1):
            if r_s1[i][j:j + M] == r_s1[i][j:j + M][::-1]:
                for i in r_s1[i][j:j + M]:
                    r_result += i
                print(f'#{tc} {r_result}')
                return ()
T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]
    palindrome(arr)
