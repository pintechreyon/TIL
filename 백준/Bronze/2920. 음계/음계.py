arr = list(map(int, input().split()))
A = [1,2,3,4,5,6,7,8]
B = [8,7,6,5,4,3,2,1]
if arr == A:
    print('ascending')
elif arr == B:
    print('descending')
else:
    print('mixed')