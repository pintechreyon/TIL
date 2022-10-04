N = int(input())
var = 666
cnt = 0
while cnt < N:
    for i in range(len(str(var))-2):
        if int(str(var)[i]) == 6 and int(str(var)[i+1]) == 6 and int(str(var)[i+2]) == 6:
            cnt += 1
            break
    var += 1
print(var-1)