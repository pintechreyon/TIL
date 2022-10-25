def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] not in answer:
            answer[i[1]] = 1
        else:
            answer[i[1]] += 1

    cnt = 1
    for i in answer.values():
        cnt *= (i + 1)
    return cnt - 1


T = int(input())
for i in range(1, T+1):
    N = int(input())
    clothes = [list(input().split()) for _ in range(N)]
    print(solution(clothes))