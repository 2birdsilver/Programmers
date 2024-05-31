from math import factorial

def solution(n):
    answer = 0

    for y in range(0, n//2+1):
        x = n - 2 * y

        if x == 0 or y == 0:
            answer += 1
        else:
            seq = int(factorial(x + y) // (factorial(x) * factorial(y)))
            answer += seq

    return answer % 1234567