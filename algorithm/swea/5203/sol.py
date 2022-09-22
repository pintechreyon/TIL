import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    p_1 = []; p_2 = []; cnt_1 = 0; cnt_2 = 0; result = 0
    flag = False
    for i in range(12):
        if flag:
            break
        if i % 2 == 0:
            p_1.append(card[i]); p_1.sort()
        else:
            p_2.append(card[i]); p_2.sort()
        if i >= 4:
            for j in range(len(p_1)-2):
                if len(p_1) == len(p_2):
                    if p_1[j] == p_1[j+1] == p_1[j+2]:
                        cnt_1 += 1
                    elif p_1[j] + 1 in p_1 and p_1[j] + 2 in p_1:
                        cnt_1 += 1
                if len(p_1) == len(p_2):
                    if p_2[j] == p_2[j + 1] == p_2[j + 2]:
                        cnt_2 += 1
                    elif p_2[j] + 1 in p_2 and p_2[j] + 2 in p_2:
                        cnt_2 += 1
                if cnt_1 == 1:
                    result = 1; flag = True
                    break
                elif cnt_2 == 1:
                    result = 2; flag = True
                    break
    print(f'#{tc} {result}')
