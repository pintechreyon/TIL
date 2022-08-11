import sys
sys.stdin = open('input.txt')

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
T = int(input())

for tc in range(1, T+1):
    num = input()
    arr = bubble_sort(list(map(int, input().split())))
    print(f'#{tc} {arr[-1]} {arr[0]} {arr[-2]} {arr[1]} {arr[-3]} {arr[2]} {arr[-4]} {arr[3]} {arr[-5]} {arr[4]}')
