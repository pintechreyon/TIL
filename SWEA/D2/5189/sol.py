import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = []
    var = []
    for i in range(N):
        if i == 0:
            continue
        for j in range(N):

