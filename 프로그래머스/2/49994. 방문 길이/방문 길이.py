def solution(dirs):
    directions = ["U","D","R","L"]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    x, y = 0, 0
    s = set()

    for dir in dirs:
        index = directions.index(dir)
        nx = x + dx[index]
        ny = y + dy[index]

        if (-5 <= nx <= 5 and -5 <= ny <= 5) :
            s.add(str(x) + str(y) + str(nx) + str(ny))
            s.add(str(nx) + str(ny) + str(x) + str(y))
            x, y = nx, ny

    return int(len(s)/2)