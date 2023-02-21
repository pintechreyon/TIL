dap = [0, 1, 1]
for i in range(3, 41):
    dap.append(dap[i-1] + dap[i-2])

T = int(input())
for tc in range(1, T+1):

    N = int(input())

    if N == 0:
        result = [1, 0]
    elif N == 1:
        result = [0, 1]
    else:
        result = [dap[N-1], dap[N]]

    print(*result)
