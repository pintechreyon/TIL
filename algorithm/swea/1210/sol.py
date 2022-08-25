import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N=int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if arr[99][i] == 2:
            col = 99
            row = i
            break
    while col > 0:
        if row - 1 >= 0 and arr[col][row-1] == 1:
            arr[col][row - 1] = 0
            row -= 1
        elif row + 1 <= 99 and arr[col][row+1] == 1:
            arr[col][row+1] = 1
            row += 1
        else:
            col -= 1
    print(f'#{tc} {row}')


