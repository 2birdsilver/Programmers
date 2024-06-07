from collections import deque

# 괄호문자열이 올바른지 확인
def right_panenthesis(s):
    stack = deque()
    before, current = '', ''
    for panenthesis in s:
        current = panenthesis
        if (current == ')' and before == '(') or current == ']' and before == '[' or current == '}' and before == '{':
            stack.pop()
            if len(stack) != 0:
                before = stack[-1]
            else:
                before = ''
        else:
            stack.append(current)
            before = current
    if len(stack) == 0:
        return True
    else:
        return False

def solution(s):
    answer = 0
    queue = deque(s)
    n = len(s)

    for i in range(n):
        current = queue.popleft()
        queue.append(current)
        if right_panenthesis(queue):
            answer += 1
    return answer