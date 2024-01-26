def solution(n):

    count = 1
    dx, dy = 0, 0  # 현재위치
    spots = [[0 for j in range(n)] for i in range(n)]  # 2차원배열
    
    while count <= n**2:
        for i in range(0, n, 1):  # 동쪽으로 이동 => dx+1
            if count > n ** 2:
                break
            if spots[dx][i] == 0:  # 행 고정
                spots[dx][i] = count
                count += 1
                dy = i
                
        for i in range(0, n, 1):  # 남쪽으로 이동 => dy+1
            if count > n ** 2:
                break
            if spots[i][dy] == 0:  # 열 고정
                spots[i][dy] = count
                count += 1
                dx = i

        for i in range(n-1, -1, -1):  # 서쪽으로 이동 => dx-1
            if count > n ** 2:
                break
            if spots[dx][i] == 0:  # 행 고정
                spots[dx][i] = count
                count += 1
                dy = i

        for i in range(n-1, -1, -1):  # 북쪽으로 이동 => dy-1
            if count > n ** 2:
                break
            if spots[i][dy] == 0:  # 열 고정
                spots[i][dy] = count
                count += 1
                dx = i

    return spots