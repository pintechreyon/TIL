T = int(input())
for tc in range(1,T+1):
    arr = list(input())
    cnt = 0
    result = ''
    for i in arr:
        if i == '1':
            cnt += 1
    if cnt % 2 == 1:
        result = 'yes'
    else:
        result = 'no'
    print(f'#{tc} {result}')