def solution(s1, s2):
    answer = 0
    s1.sort(reverse=True)
    s2.sort(reverse=True)
    for i in s2:
        for j in range(len(s1)):
            if i > s1[j]:
                answer += 1
                s1.pop(j)
                break
    return answer