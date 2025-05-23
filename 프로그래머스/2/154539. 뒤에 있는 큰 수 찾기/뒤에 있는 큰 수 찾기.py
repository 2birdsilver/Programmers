import heapq

def solution(numbers):
    q = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)-1, -1, -1):
        number = numbers[i]
        while q:
            if q[0] > number:
                answer[i] = q[0]
                break
            else: heapq.heappop(q)
        heapq.heappush(q, number)

    return answer