import sys
sys.stdin = open('input.txt')
N = int(input())
lst = []
for i in range(N):
    lst.append(input())
r_arr = set(lst)
arr = sorted(list(r_arr))
var = [0] * len(arr)
for i in range(len(arr)):
    for j in lst:
        if list(arr)[i] == j:
            var[i] += 1
result = list(arr)[var.index(max(var))]
print(result)

