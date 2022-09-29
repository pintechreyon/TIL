N = int(input())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
arr_a.sort()
arr_b.sort(reverse=True)
result = 0
for i in range(N):
    var = arr_a[i] * arr_b[i]
    result += var
print(result)