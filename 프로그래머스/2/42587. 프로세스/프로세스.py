from collections import deque

def solution(priorities, location):
    answer = 0
    stack = deque(sorted(priorities))
    q = deque()

    for i in range(len(priorities)):
        q.append((priorities[i], 65+i))

    property = stack.pop()
    while q:
        process = q.popleft()
        if process[0] == property:
            answer += 1
            if len(q) != 0:
                property = stack.pop()
            if chr(process[1]) == chr(location+65):
                return answer
        else:
            q.append(process)