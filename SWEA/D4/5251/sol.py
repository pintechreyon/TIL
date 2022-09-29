test_case = int(input())
for tc in range(test_case):
    V, E = map(int, input().split())
    INF = 987654321
    graph = [[INF for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        a, b, w = map(int, input().split())

        graph[a][b] = w

    dp = [INF] * (V+1)
    dp[0] = 0

    for a in range(V+1):
        for b in range(V+1):
            if dp[a] + graph[a][b] < dp[b]:
                dp[b] = dp[a] + graph[a][b]

    answer = dp[V]
    print(f'#{tc+1} {answer}')