import sys
sys.stdin = open('input.txt')

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

T = int(input())

for tc in range(1, T+1):
    N1, N2 = list(input().split())
    arr = list(input().split())
    dict = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    R_dict = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}
    result = []
    end = ''
    for i in range(int(N2)):
            result.append(dict[arr[i]])
    bubble_sort(result)
    for i in range(len(result)):
        end += (R_dict[result[i]] + ' ')
    print(f'#{tc}')
    print(end)