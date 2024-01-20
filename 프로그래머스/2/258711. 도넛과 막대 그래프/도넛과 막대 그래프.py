def solution(edges):
    solnum = 0
    doughnut = 0
    stick = 0
    eight = 0
    maxnum = 0
    inputnum = [0 for i in range(1000001)]
    outputnum = [0 for i in range(1000001)]
    for b, a in edges:
        inputnum[a] += 1
        outputnum[b] += 1
        if a > maxnum:
            maxnum = a
    for i in range(1,maxnum+1):
        if inputnum[i] == 0 and outputnum[i] >= 2:
            solnum = i
        elif inputnum[i] >= 2 and outputnum[i] == 2:
            eight += 1
        elif outputnum[i] == 0:
            stick += 1
    doughnut = outputnum[solnum] - eight - stick
        
    answer = [solnum,doughnut,stick,eight]
    return answer