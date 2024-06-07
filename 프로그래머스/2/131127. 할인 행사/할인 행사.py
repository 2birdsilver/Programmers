import copy
from collections import deque
from copy import deepcopy

def isDiscountDay(want, number, q):
    for i in range(10):
        item = q.popleft()
        if item in want:
            item_index = want.index(item)
            number[item_index] -= 1

    if number.count(0) == len(number):
        return True
    else:
        return False
def solution(want, number, discount):
    answer = 0
    q = deque(discount[0:10], maxlen=10) # queue초기화
    if isDiscountDay(want, copy.deepcopy(number), copy.deepcopy(q)):
        answer += 1

    for d in discount[10:]:
        q.popleft()
        q.append(d)
        if isDiscountDay(want, copy.deepcopy(number), copy.deepcopy(q)):
            answer += 1
    return answer