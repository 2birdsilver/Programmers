import math


def solution(str1, str2):
    answer = 0
    list_str1 = makeList(str1)
    list_str2 = makeList(str2)
    if (len(list_str1) == 0 and len(list_str2) == 0):
        return 65536

    list_str1_copy  = list_str1.copy()

    # 리스트 교집합 구하기
    intersection_list = list()
    for pair in list_str1_copy:
        if pair in list_str2:
            intersection_list.append(pair)
            list_str1.remove(pair)
            list_str2.remove(pair)

    union_list = intersection_list + list_str1 + list_str2

    answer = math.floor(len(intersection_list) / len(union_list) * 65536)


    return answer


def makeList(str):

    first_list = list()
    fore_letter = str[0]

    # 2문자씩 쌍 만들기
    for i in range(1, len(str)):
        letter_pair = fore_letter + str[i]
        first_list.append(letter_pair)
        fore_letter = str[i]

    # 문자열에서 첫 알파벳 저장
    index = 0
    new_list = list()
    for pair in first_list:
        if pair.isalpha():
            new_list.append(pair.upper())

    return new_list