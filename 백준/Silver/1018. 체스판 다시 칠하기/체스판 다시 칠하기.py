row, col = map(int, input().split())
arr = [list(input()) for _ in range(row)]
white = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
black = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
maxv = 64
for i in range(row-7):
    for j in range(col-7):
        for k in range(2):
            cnt = 0
            if k == 0:
                for t in range(8):
                    for g in range(8):
                        if t % 2 == 0:
                            if white[g] != arr[i+t][j+g]:
                                cnt += 1
                        if t % 2 == 1:
                            if black[g] != arr[i + t][j + g]:
                                cnt += 1
                if cnt < maxv:
                    maxv = cnt
            if k == 1:
                for t in range(8):
                    for g in range(8):
                        if t % 2 == 1:
                            if white[g] != arr[i+t][j+g]:
                                cnt += 1
                        if t % 2 == 0:
                            if black[g] != arr[i + t][j + g]:
                                cnt += 1
                if cnt < maxv:
                    maxv = cnt
print(maxv)