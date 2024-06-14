from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque(maxlen=cacheSize)

    for city in cities:
        city = city.lower()
        if q.count(city) != 0:
            answer += 1
            q.remove(city)
        else:
            answer += 5

        q.append(city)

    return answer