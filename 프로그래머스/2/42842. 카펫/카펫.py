def solution(brown, yellow):
    answer = []

    x, y = 0, 0
    for i in range(2000000):
        if i * i + i * (2-brown//2) + yellow == 0:
            x = i
            y = brown // 2 - 2 - x
            answer.append(max(x, y) + 2)
            answer.append(min(x, y) + 2)
            return answer