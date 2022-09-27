import sys
sys.stdin = open('input.txt')

def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return data[mid]
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search_recursion(target, start, end, data)

T = int(input())
for tc in range(1,T+1):
    A, B = map(int, input().split())
    A_arr = list(map(int, input().split()))
    A_arr.sort
    B_arr = list(map(int, input().split()))
    result = 0
    for i in B_arr:
        if binary_search_recursion(i, 0, len(A_arr)-1, A_arr):
            result += 1
    print(f'#{tc} {result}')