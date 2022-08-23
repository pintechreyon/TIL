import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if arr[i][0] == 1:

