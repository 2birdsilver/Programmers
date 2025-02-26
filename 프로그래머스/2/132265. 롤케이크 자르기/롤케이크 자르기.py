from collections import deque

def initMap(list):
    mySet = set(list)
    dict = {}

    for item in mySet:
        dict[item] = 0

    return dict

def solution(topping):
    result = 0
    q = deque(topping)
    count1 = len(set(topping))
    count2 = 0
    map2 = initMap(topping)
    map1 = map2.copy()

    # 토핑 수에 따른 map 초기화
    for i in topping:
        map1[i] += 1

    while q:
        num = q.popleft()
        map1[num] -= 1
        if map1[num] == 0:
            count1 -= 1
        map2[num] += 1
        if map2[num] == 1:
            count2 += 1
        if count1 == count2:
            result += 1

    return result