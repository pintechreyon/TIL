import sys
sys.stdin = open('input.txt')

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    not_pivot = arr[1:]
    left_side = []
    right_side = []
    for i in not_pivot:
        if i <= pivot:
            left_side.append(i)
        else:
            right_side.append(i)
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    lst = list(map(int, input().split()))
    result = quick_sort(lst)
    print(f'#{tc} {result[N//2]}')

