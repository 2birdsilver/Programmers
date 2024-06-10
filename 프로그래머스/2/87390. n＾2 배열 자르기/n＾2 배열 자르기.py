def solution(n, left, right):
    answer = []

    for i in range(left, right+1):
        share = i // n
        remain = i % n
        value = max(share, remain) + 1
        answer.append(value)

    return answer