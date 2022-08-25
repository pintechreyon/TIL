import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int, input().split()))
    oven = []
    cnt = 0
    pizza = []
    pizza_oven = []
    for i in range(1,M+1):
        pizza.append(i)
    for i in range(N):
        oven.append(arr[i])
        pizza_oven.append(pizza[i])
    while len(oven) > 1:
        if oven[0]  <= 1:
            if cnt < M-N:
                oven.append(arr[-(M-N-cnt)])
                pizza_oven.append(pizza[-(M - N - cnt)])
                cnt += 1
                oven.pop(0)
                pizza_oven.pop(0)
            else:
                oven.pop(0)
                pizza_oven.pop(0)
        else:
            oven[0] = oven[0] // 2
            oven.append(oven[0])
            pizza_oven.append(pizza_oven[0])
            oven.pop(0)
            pizza_oven.pop(0)
    print(f'#{tc} {pizza_oven[0]}')


