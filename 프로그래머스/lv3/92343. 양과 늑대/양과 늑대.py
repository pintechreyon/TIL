from collections import deque


def solution(info, edges):
    n = len(info)
    tree = [[] for _ in range(n)]
    answer = 1 

    for edge in edges:
        tree[edge[0]].append(edge[1])

    queue = deque([[tree[0], 1, 1]])  

    while queue:
        data = queue.popleft()

        for idx, next_node in enumerate(data[0]):

            total = data[2]
            if info[next_node] == 0:  
                cal = data[1] + 1
                total += 1

            else:
                cal = data[1] - 1 

            if cal > 0:  
                queue.append([data[0][:idx] + data[0][idx+1:] + tree[next_node], cal, total])
                answer = max(answer, total)

    return answer
