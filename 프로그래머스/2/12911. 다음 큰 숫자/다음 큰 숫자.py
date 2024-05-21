def solution(n):
    binary_n = format(n, 'b')
    list_n = list(binary_n)
    one_count_n = list_n.count('1')

    one_count_y = 0
    y = n

    while one_count_n != one_count_y:
        y += 1
        binary_y = format(y, 'b')
        list_y = list(binary_y)
        one_count_y = list_y.count('1')

    return y