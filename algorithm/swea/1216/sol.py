import sys
sys.stdin = open('input.txt')


def palindrome(s1):
    r_s1 = list(zip(*s1))
    maxv = 0
    for k in range(100):
        for i in range(100):
            for j in range(i, 100):
                if s1[k][i:j + 1] == s1[k][j:i - 1:-1]:
                    if maxv < len(s1[k][i:j + 1]):
                        maxv = len(s1[k][i:j + 1])
    for k in range(100):
        for i in range(100):
            for j in range(i, 100):
                if r_s1[k][i:j + 1] == r_s1[k][j:i - 1:-1]:
                    if maxv < len(r_s1[k][i:j + 1]):
                        maxv = len(r_s1[k][i:j + 1])
    print(f'#{tc} {maxv}')
T = 10

for tc in range(1, T+1):
    no_sseulmo = input()
    arr = [input() for _ in range(100)]
    palindrome(arr)
