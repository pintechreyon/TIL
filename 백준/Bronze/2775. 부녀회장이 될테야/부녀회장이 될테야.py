import sys
            
T = int(sys.stdin.readline().rstrip())
for tc in range(1,T+1):
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    cnt = 1
    while cnt <= N:
        for i in range(len(nums)-1,0,-1):
            nums[i] = sum(nums[:i+1])
        cnt += 1
    print(nums[M])