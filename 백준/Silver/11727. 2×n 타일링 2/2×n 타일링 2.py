result = [0, 1, 3]
N = int(input())
if N > 2:
    for i in range(3, N+1):
        result.append(result[i-1] + result[i-2] + result[i-2])

dap = result[N] % 10007
print(dap)
