T = int(input())
for tc in range(1, 1+T):
    N, M = input().split()
    N = int(N)
    word = ''
    for i in M:
        word += (i*N)
    print(word)