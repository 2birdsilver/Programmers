def solution(clothes):
    dic = dict()

    # 딕셔너리에 의상수 저장
    for costume in clothes:
        if costume[1] in dic.keys():
            dic[costume[1]] += 1
        else:
            dic[costume[1]] = 1

    answer = 1
    for count in dic.values():
        answer *= (count + 1)

    return answer - 1
