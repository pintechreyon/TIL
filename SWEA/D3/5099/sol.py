import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int, input().split()))
#오븐에 들어간 피자의 치즈 양
    oven = []
    cnt = 0
#피자들의 이름
    pizza = []
#오븐에 들어간 피자의 이름
    pizza_oven = []
#피자에 이름을 붙여준다
    for i in range(1,M+1):
        pizza.append(i)
#N개만큼 피자를 오븐에 넣어준다
    for i in range(N):
        oven.append(arr[i])
#들어간 피자의 이름을 따로 넣어준다
        pizza_oven.append(pizza[i])
#피자가 1개남을때까지 돌려돌려 돌림판
    while len(oven) > 1:
#오븐의 치즈가 1이하면 오븐에서 빼줘야함
        if oven[0]  <= 1:
            if cnt < M-N:
#뒤에 대기하고 있는 피자를 넣어준다(이름도 같이)
                oven.append(arr[-(M-N-cnt)])
                pizza_oven.append(pizza[-(M - N - cnt)])
                cnt += 1
#치즈가 다 녹은 피자는 빼준다
                oven.pop(0)
                pizza_oven.pop(0)
#cnt가 M - N보다 커지면 이미 들어간 피자를 부활시키므로 넘으면 다녹은 피자만 빼준다
            else:
                oven.pop(0)
                pizza_oven.pop(0)
#치즈가 덜 녹았으면 절반만큼 녹은것을 확인하고 다시 돌려준다
        else:
            oven[0] = oven[0] // 2
            oven.append(oven[0])
            pizza_oven.append(pizza_oven[0])
            oven.pop(0)
            pizza_oven.pop(0)
#오븐에 피자가 하나 남았을때 피자의 이름을 출력한다
    print(f'#{tc} {pizza_oven[0]}')