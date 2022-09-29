import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    arr = list(input().split())
    arr.pop()
    num_stack = []
    stack = []
    lst = []
    giho = ['+','-','/','*']
    for i in arr:
        if i in giho:
            lst.append(i)
        else:
            num_stack.append(i)
    for i in range(len(arr)):
        if len(num_stack) - 1 != len(lst):
            stack.append('error')
            break
        elif arr[i] in giho:
            if arr[i] == '+':
                stack[-2] = stack[-1] + stack[-2]
                stack.pop()
            elif arr[i] == '-':
                stack[-2] = stack[-2] - stack[-1]
                stack.pop()
            elif arr[i] == '*':
                stack[-2] = stack[-1] * stack[-2]
                stack.pop()
            elif arr[i] == '/':
                stack[-2] = stack[-2] // stack[-1]
                stack.pop()
        else:
            stack.append(int(arr[i]))
    print(f'#{tc} {stack[0]}')