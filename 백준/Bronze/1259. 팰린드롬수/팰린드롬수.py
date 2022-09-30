while True:
    N = input()
    if N == '0':
        break
    R = N[::-1]
    for i in range(len(N)):
        if N[i] != R[i]:
            print('no')
            break
    else:
        print('yes')