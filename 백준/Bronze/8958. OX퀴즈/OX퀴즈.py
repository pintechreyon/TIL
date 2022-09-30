T = int(input())
for tc in range(1, T+1):
    arr = input()
    cnt = 0
    result = 0
    for i in arr:
        if i == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)