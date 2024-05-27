from collections import deque

def solution(s):
    stack = deque()
    if len(s) % 2 == 1:
        return 0

    alphabet_dic = {}
    for alphabet in s:
        if alphabet in alphabet_dic:
            alphabet_dic[alphabet] += 1
        else:
            alphabet_dic[alphabet] = 1

    for element in alphabet_dic.keys():
        if alphabet_dic[element] % 2 == 1:
            return 0


    for i in range(len(s)):
        if len(stack) != 0 and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
        previous = s[i]

    if len(stack) == 0:
        return 1
    else:
        return 0