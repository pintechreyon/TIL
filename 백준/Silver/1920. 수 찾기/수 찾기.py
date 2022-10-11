import sys

def binary(n_list, target):
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if n_list[mid] == target:
            return True

        if target < n_list[mid]:
            right = mid-1
        elif target > n_list[mid]:
            left = mid + 1


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
M = int(sys.stdin.readline())
for i in list(map(int, sys.stdin.readline().split())):
    if binary(arr, i):
        print(1)
    else:
        print(0)