import math
def solution(n, words):
    length = len(words)
    copy = []
    answer = []
    isLeavingOut = False

    current = ''
    before = ''
    i = 0
    for i in range(length):
        current = words[i]

        # 중복되는 값이 있는 경우
        if copy.count(current) > 0:
            isLeavingOut = True
            break

        # 이전 단어의 마지막문자와 동일하지 않은 경우
        if len(before) >= 1 and before[-1] != current[0]:
            isLeavingOut = True
            break

        copy.append(current)
        before = current

    num = 0 if i == length-1 and isLeavingOut == False else i % n + 1
    count = 0 if i == length-1 and isLeavingOut == False else i // n + 1

    answer.append(num)
    answer.append(count)

    return answer