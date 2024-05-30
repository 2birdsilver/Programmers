def solution(people, limit):
    answer = 0
    people.sort()

    # 인원이 2명 이상인 경우, 가장 가벼운사람과 가장 무거운사람의 무게합이 limit이하인지 확인한다.
    heavy_index = len(people) - 1
    lighy_index = 0
    for i in range(len(people)):
        if heavy_index == lighy_index:
            return answer + 1

        if lighy_index > heavy_index:
            return answer

        if people[heavy_index] + people[lighy_index] <= limit:
            lighy_index += 1
        heavy_index -= 1
        answer += 1
    return answer