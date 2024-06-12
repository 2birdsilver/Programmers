def solution(arr1, arr2):
    arr2 = change_matrix(arr2)
    answer = [[]for _ in range(len(arr1))]

    for i in range(len(arr1)):
        list1 = arr1[i]
        for j in range(len(arr2)):
            list2 = arr2[j]
            value = multifly(list1, list2)
            answer[i].append(value)

    return answer

# 배열의 행과 열을 서로 바꾸기
def change_matrix(arr):
    result = [[] for _ in range(len(arr[0]))]
    list = []
    for l in arr:
        for i in range(len(l)):
            result[i].append(l[i])
    return result

# 두 리스트의 곱
def multifly(list1, list2):
    n = len(list1)
    sum = 0
    for i in range(n):
        sum += list1[i] * list2[i]
    return sum