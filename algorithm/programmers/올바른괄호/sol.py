def solution(s):
    answer = True

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        elif stack and i == ')':
            stack.pop()
        elif not stack and i == ')':
            return False
    if len(stack) > 0:
        return False

    return True