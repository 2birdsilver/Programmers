from queue import PriorityQueue
def solution(k, tangerine):
    max_value = max(tangerine)
    classfication = [0] * (max_value+1)

    for tan in tangerine:
        classfication[tan] += 1

    classfication.sort()
    count = 0
    types = 0
    while True:
        if count >= k:
            return types
        count += classfication.pop()
        types += 1