def solution(n):
    answer = 0

    num_table = [0] * 10001

    for i in range(2,10000):
        num_table[i] = num_table[i-1] + (i-1)


    for i in range(1, n+1):
        if num_table[i] >= n:
            return answer
        if (n - num_table[i]) % i == 0:
            answer += 1

    return answer