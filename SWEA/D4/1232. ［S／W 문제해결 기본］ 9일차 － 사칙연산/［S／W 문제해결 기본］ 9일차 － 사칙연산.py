for tc in range(1,11):
    V = int(input())
    arr = [list(input().split()) for i in range(V)]
    tree = [0] * (V + 1)
    arr.insert(0,[0,0,0,0])
    for i in arr:
        if len(i) == 4:
            tree[int(i[0])] = i[1]
        else:
            tree[int(i[0])] = int(i[1])
    for i in range(V, 0, -1):
        if type(tree[i]) != int:
            if tree[i] == '+':
                tree[i] = tree[int(arr[i][2])] + tree[int(arr[i][3])]
            elif tree[i] == '-':
                tree[i] = tree[int(arr[i][2])] - tree[int(arr[i][3])]
            elif tree[i] == '*':
                tree[i] = tree[int(arr[i][2])] * tree[int(arr[i][3])]
            else:
                tree[i] = tree[int(arr[i][2])] / tree[int(arr[i][3])]
    print(f'#{tc} {int(tree[1])}')
