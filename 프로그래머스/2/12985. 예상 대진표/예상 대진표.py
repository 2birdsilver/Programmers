import math


def solution(n,a,b):
    answer = 0

    while True:
        answer += 1
        a = int(math.ceil(a / 2.0))
        b = int(math.ceil(b / 2.0))

        if a == b:
            break

    return answer