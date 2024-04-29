def solution(s):
    input_value = list(map(int,s.split()))
    min = input_value[0]
    max = input_value[0]

    for num in input_value:
        if min > num:
            min = num
        if max < num:
            max = num

    answer = str(min) + ' ' + str(max)
    return answer