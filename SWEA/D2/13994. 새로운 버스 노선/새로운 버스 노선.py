T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sta = [[] for i in range(N)]
    cnt = 0
    result = 0
    var = 0
    ED = []
    for i in arr:
        A, B, C = i
        if A == 1:
            for j in range(B, C+1):
                sta[cnt].append(j)
        if A == 2:
            if B % 2 == 0:
                for j in range(B+1, C):
                    if j % 2 == 0:
                        sta[cnt].append(j)
                sta[cnt] = [B] + sta[cnt] + [C]
            if B % 2 == 1:
                for j in range(B+1, C):
                    if j % 2 == 1:
                        sta[cnt].append(j)
                sta[cnt] = [B] + sta[cnt] + [C]
        if A == 3:
            if B % 2 == 0:
                for j in range(B+1, C):
                    if j % 4 == 0:
                        sta[cnt].append(j)
                sta[cnt] = [B] + sta[cnt] + [C]
            if B % 2 == 1:
                for j in range(B+1, C):
                    if j % 3 == 0 and j % 10 != 0:
                        sta[cnt].append(j)
                sta[cnt] = [B] + sta[cnt] + [C]
        cnt += 1
    for i in sta:
        ED += i
    ED = set(ED)
    for i in ED:
        var = 0
        for j in range(N):
            if i in sta[j]:
                var += 1
        if result < var:
            result = var
    print(f'#{tc} {result}')


