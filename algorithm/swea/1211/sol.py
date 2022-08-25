import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    row_lst = []
    maxv = 10000
    result = 0
    for i in range(100):
        if arr[0][i] == 1:
            row_lst.append(i)
    for row in row_lst:
        cnt = 0
        col = 0
        var = row
        while col < 99:
            if row - 1 >= 0 and arr[col][row - 1] == 1:
                while row - 1 >= 0 and arr[col][row - 1] == 1:
                    row -= 1
                    cnt += 1
            elif row + 1 <= 99 and arr[col][row + 1] == 1:
                while row + 1 <= 99 and arr[col][row + 1] == 1:
                    row += 1
                    cnt += 1
            col += 1
        if maxv > cnt:
            maxv = cnt
            result = var
    print(f'#{tc} {result}')
