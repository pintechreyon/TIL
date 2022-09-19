import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    pat = input()
    arr = 'abcdefghijklmnopqrstuvwxyz'
    cnt = 0
    if len(pat) > 26:
        pat = pat[:26]
    elif len(pat) <= 26:
        arr = arr[:len(pat)]

    for i in range(len(pat)):
        if i == 0:
            if pat[i] == arr[i]:
                cnt += 1
        elif pat[i-1] == arr[i-1]:
            if pat[i] == arr[i]:
                cnt += 1
            else:
                break
        else:
            break
    print(f'#{tc} {cnt}')