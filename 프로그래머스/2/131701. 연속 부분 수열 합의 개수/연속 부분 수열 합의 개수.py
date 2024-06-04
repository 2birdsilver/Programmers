from collections import deque


def solution(elements):
    n = len(elements)
    sums = set()

    for i in range(1, n+1):
        q = deque(maxlen=i)

        for num in elements * 2:
            q.append(num)
            sums.add(sum(q))


    return len(sums)