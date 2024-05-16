def solution(s):
    answer = []
    zero_cnt = 0
    conversion_cnt = 0

    while (s != "1"):
        zero_cnt += s.count('0')
        s = s.replace('0','')

        length = len(s)
        s = format(length, 'b')
        conversion_cnt += 1

    answer.append(conversion_cnt)
    answer.append(zero_cnt)

    return answer